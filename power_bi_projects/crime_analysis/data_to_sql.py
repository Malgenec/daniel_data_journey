from datetime import datetime
import pymysql
import sys
import os
import time

def to_int(val):
    # Convert string to integer, return None if invalid
    val = val.strip() if val else ""
    return int(val) if val.isdigit() else None

def to_decimal(val):
    # Convert string to decimal for property values
    val = val.strip() if val else ""
    try:
        return float(val) if val else None
    except:
        return None

def to_date(val):
    # Convert YYYYMMDD string to date object
    val = val.strip() if val else ""
    if not val or val == '00000000':
        return None
    try:
        return datetime.strptime(val, "%Y%m%d").date()
    except:
        return None

def to_str(val):
    # Return a clean string value
    result = val.strip() if val else None
    return result if result else None

def extract_repeating_field(line, start, length, count):
    # Extract repeating fields and return as comma-separated string
    values = []
    for i in range(count):
        pos = start + (i * length)
        val = to_str(line[pos:pos + length])
        if val:
            values.append(val)
    return ','.join(values) if values else None

def extract_monthly_activities(line, start):
    # Extract 12 months of activity indicators (3 chars each)
    activities = []
    for month in range(12):
        pos = start + (month * 3)
        zero_report = line[pos:pos + 1]
        group_ab = line[pos + 1:pos + 2]
        window = line[pos + 2:pos + 3]
        activities.append({
            'month': month + 1,
            'zero_report': to_str(zero_report),
            'group_ab': to_str(group_ab),
            'window': to_str(window)
        })
    return activities

def format_eta(seconds):
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        m, s = divmod(int(seconds), 60)
        return f"{m}m {s}s"
    else:
        h, remainder = divmod(int(seconds), 3600)
        m, s = divmod(remainder, 60)
        return f"{h}h {m}m {s}s"

def format_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"

def create_connection():
    # Create MySQL database connection
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="password", # Changed password for obvious reasons :D
            database="nibrs",
            charset='utf8mb4'
        )
        return conn
    except Exception as e:
        print(f"ERROR: Could not connect to database: {e}")
        sys.exit(1)

# ============================================================================
# RECORD PROCESSORS
# ============================================================================

def process_batch_header(line, cursor, batch_header_cache):
    # Process BH/B2/B3 records (batch headers, long story short - b2 and b3 is not really needed type of information for this project, could have skipped that)
    segment = line[0:2]
    state_code = to_str(line[2:4])
    ori = to_str(line[4:13])
    
    key = f"{state_code}_{ori}"
    
    if segment == "BH":
        # BH - Main batch header
        cursor.execute("""
            INSERT INTO batch_header (
                segment_level, state_code, ori, ori_date_added, ori_date_went_nibrs,
                city, state_abbreviation, population_group, country_division, country_region,
                agency_indicator, core_city, covered_by_ori, fbi_field_office, judicial_district,
                agency_nibrs_flag, agency_inactive_date, county_population_coverage,
                report_period_indicator, report_months_amount, master_file_year, fips_county_codes
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            segment,
            state_code,
            ori,
            to_date(line[25:33]),    # ori_date_added
            to_date(line[33:41]),    # ori_date_went_nibrs
            to_str(line[41:71]),     # city
            to_str(line[71:73]),     # state_abbreviation
            to_str(line[73:75]),     # population_group
            to_str(line[75:76]),     # country_division
            to_str(line[76:77]),     # country_region
            to_str(line[77:78]),     # agency_indicator
            to_str(line[78:79]),     # core_city
            to_str(line[79:88]),     # covered_by_ori
            to_str(line[88:92]),     # fbi_field_office
            to_str(line[92:96]),     # judicial_district
            to_str(line[96:97]),     # agency_nibrs_flag
            to_date(line[97:105]),   # agency_inactive_date
            to_str(line[105:225]),   # county_population_coverage (120 chars)
            to_str(line[225:227]),   # report_period_indicator
            to_int(line[227:229]),   # report_months_amount
            to_str(line[229:233]),   # master_file_year
            extract_repeating_field(line, 269, 3, 5)  # fips_county_codes
        ))
        
        # Get the inserted ID for later use
        batch_id = cursor.lastrowid
        batch_header_cache[key] = {
            'id': batch_id,
            'monthly_activities': extract_monthly_activities(line, 233)
        }
        
    elif segment == "B2":
        # B2 - Additional county population coverage
        if key in batch_header_cache:
            cursor.execute("""
                UPDATE batch_header
                SET county_population_coverage = CONCAT(IFNULL(county_population_coverage, ''), %s)
                WHERE id = %s
            """, (
                to_str(line[25:121]),  # Additional 96 chars
                batch_header_cache[key]['id']
            ))
    
    elif segment == "B3":
        # B3 - Final batch header data
        if key in batch_header_cache:
            cursor.execute("""
                UPDATE batch_header
                SET county_population_coverage = CONCAT(IFNULL(county_population_coverage, ''), %s)
                WHERE id = %s
            """, (
                to_str(line[25:49]),  # Final 24 chars
                batch_header_cache[key]['id']
            ))

def process_incident(line, cursor):
    # Process 01 and W1 records
    cursor.execute("""
        INSERT INTO incident (
            segment_level, state_code, ori, incident_number, incident_date,
            report_date_indicator, incident_hour, total_offense_segments,
            total_victim_segments, total_offender_segments, total_arrestee_segments,
            city_submission, cleared_exceptionally, exceptional_clearance_date, ucr_offense_codes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        to_str(line[0:2]),           # segment_level (01 or W1)
        to_str(line[2:4]),           # state_code
        to_str(line[4:13]),          # ori
        to_str(line[13:25]),         # incident_number
        to_date(line[25:33]),        # incident_date
        to_str(line[33:34]),         # report_date_indicator
        to_str(line[34:36]),         # incident_hour
        to_int(line[36:38]),         # total_offense_segments
        to_int(line[38:41]),         # total_victim_segments
        to_int(line[41:43]),         # total_offender_segments
        to_int(line[43:45]),         # total_arrestee_segments
        to_str(line[45:49]),         # city_submission
        to_str(line[49:50]),         # cleared_exceptionally
        to_date(line[50:58]),        # exceptional_clearance_date
        extract_repeating_field(line, 58, 3, 10)  # ucr_offense_codes (10 codes)
    ))
    return cursor.lastrowid

def process_offense(line, cursor):
    # Process 02 records
    cursor.execute("""
        INSERT INTO offense (
            state_code, ori, incident_number, incident_date, ucr_offense_code,
            offense_indicator, offender_suspected_of_using, location_type,
            number_of_premises_entered, method_of_entry, criminal_activities, bias_motivation
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        to_str(line[2:4]),           # state_code
        to_str(line[4:13]),          # ori
        to_str(line[13:25]),         # incident_number
        to_date(line[25:33]),        # incident_date
        to_str(line[33:36]),         # ucr_offense_code
        to_str(line[36:37]),         # offense_indicator
        to_str(line[37:40]),         # offender_suspected_of_using
        to_str(line[40:42]),         # location_type
        to_str(line[42:44]),         # number_of_premises_entered
        to_str(line[44:45]),         # method_of_entry
        extract_repeating_field(line, 45, 1, 3),  # criminal_activities (3 codes)
        to_str(line[57:59])          # bias_motivation
    ))
    
    offense_id = cursor.lastrowid
    
    # Extract weapons (3 weapons, 3 chars each)
    weapons = []
    for i in range(3):
        pos = 48 + (i * 3)
        weapon_code = to_str(line[pos:pos + 3])
        if weapon_code:
            weapons.append((offense_id, i + 1, weapon_code))
    
    if weapons:
        cursor.executemany("""
            INSERT INTO offense_weapons (offense_id, weapon_sequence, weapon_code)
            VALUES (%s, %s, %s)
        """, weapons)

def process_property(line, cursor):
    # Process 03 and W3 records
    segment = to_str(line[0:2])
    
    cursor.execute("""
        INSERT INTO property (
            segment_level, state_code, ori, incident_number, incident_date,
            type_property_loss, number_stolen_vehicles, number_recovered_vehicles, ucr_offense_codes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        segment,
        to_str(line[2:4]),           # state_code
        to_str(line[4:13]),          # ori
        to_str(line[13:25]),         # incident_number
        to_date(line[25:33]),        # incident_date
        to_str(line[33:34]),         # type_property_loss
        to_int(line[53:55]),         # number_stolen_vehicles
        to_int(line[55:57]),         # number_recovered_vehicles
        extract_repeating_field(line, 102, 3, 10) if segment == 'W3' else None  # ucr_offense_codes for W3
    ))
    
    property_id = cursor.lastrowid
    
    # Extract property items (up to 10)
    items = []
    for i in range(10):
        # Property description at position 35-36, then repeats
        desc_pos = 34 + (i * 17)  # Each property item is 17 chars
        if desc_pos + 17 <= len(line):
            prop_desc = to_str(line[desc_pos:desc_pos + 2])
            prop_value = to_decimal(line[desc_pos + 2:desc_pos + 11])
            date_recovered = to_date(line[desc_pos + 11:desc_pos + 19]) if desc_pos + 19 <= len(line) else None
            
            if prop_desc:
                items.append((property_id, i + 1, prop_desc, prop_value, date_recovered))
    
    if items:
        cursor.executemany("""
            INSERT INTO property_items (property_id, item_sequence, property_description, value_of_property, date_recovered)
            VALUES (%s, %s, %s, %s, %s)
        """, items)
    
    # Extract drug information (up to 3 drug types, 15 chars each)
    drugs = []
    for i in range(3):
        pos = 57 + (i * 15)
        if pos + 15 <= len(line):
            drug_type = to_str(line[pos:pos + 2])
            if drug_type:
                quantity = to_int(line[pos + 2:pos + 11])
                quantity_frac = to_int(line[pos + 11:pos + 14])
                measurement = to_str(line[pos + 14:pos + 15])
                drugs.append((property_id, i + 1, drug_type, quantity, quantity_frac, measurement))
    
    if drugs:
        cursor.executemany("""
            INSERT INTO property_drugs (property_id, drug_sequence, suspected_drug_type, 
                                       estimated_quantity, estimated_quantity_fractional, type_measurement)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, drugs)

def process_victim(line, cursor):
    # Process 04 records
    cursor.execute("""
        INSERT INTO victim (
            state_code, ori, incident_number, incident_date, victim_sequence_number,
            victim_connected_to, type_of_victim, victim_age, victim_sex, victim_race,
            victim_ethnicity, victim_resident_status, circumstances, justifiable_homicide_circumstances,
            type_injury, type_of_activity, assignment_type, ori_other_jurisdiction
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        to_str(line[2:4]),           # state_code
        to_str(line[4:13]),          # ori
        to_str(line[13:25]),         # incident_number
        to_date(line[25:33]),        # incident_date
        to_int(line[33:36]),         # victim_sequence_number
        extract_repeating_field(line, 36, 3, 10),  # victim_connected_to (10 UCR codes)
        to_str(line[66:67]),         # type_of_victim
        to_str(line[67:69]),         # victim_age
        to_str(line[69:70]),         # victim_sex
        to_str(line[70:71]),         # victim_race
        to_str(line[71:72]),         # victim_ethnicity
        to_str(line[72:73]),         # victim_resident_status
        extract_repeating_field(line, 73, 2, 2),  # circumstances (2 codes)
        to_str(line[77:78]),         # justifiable_homicide_circumstances
        extract_repeating_field(line, 78, 1, 5),  # type_injury (5 codes)
        to_str(line[123:125]),       # type_of_activity
        to_str(line[125:126]),       # assignment_type
        to_str(line[126:135])        # ori_other_jurisdiction
    ))
    
    victim_id = cursor.lastrowid
    
    # Extract victim-offender relationships (up to 10)
    relationships = []
    for i in range(10):
        pos = 83 + (i * 4)
        if pos + 4 <= len(line):
            offender_num = to_int(line[pos:pos + 2])
            relationship = to_str(line[pos + 2:pos + 4])
            if offender_num is not None and relationship:
                relationships.append((victim_id, offender_num, relationship))
    
    if relationships:
        cursor.executemany("""
            INSERT INTO victim_offender_relationships (victim_id, offender_number, relationship_code)
            VALUES (%s, %s, %s)
        """, relationships)

def process_offender(line, cursor):
    # Process 05 records
    cursor.execute("""
        INSERT INTO offender (
            state_code, ori, incident_number, incident_date, offender_sequence_number,
            offender_age, offender_sex, offender_race
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        to_str(line[2:4]),           # state_code
        to_str(line[4:13]),          # ori
        to_str(line[13:25]),         # incident_number
        to_date(line[25:33]),        # incident_date
        to_int(line[33:35]),         # offender_sequence_number
        to_str(line[35:37]),         # offender_age
        to_str(line[37:38]),         # offender_sex
        to_str(line[38:39])          # offender_race
    ))

def process_arrestee(line, cursor):
    # Process 06 and W6 records
    segment = to_str(line[0:2])
    
    cursor.execute("""
        INSERT INTO arrestee (
            segment_level, state_code, ori, incident_number, incident_date,
            arrestee_sequence_number, arrest_transaction_number, arrest_date, arrest_type,
            multiple_arrestee_indicator, ucr_arrest_offense_code, arrestee_age, arrestee_sex,
            arrestee_race, arrestee_ethnicity, arrestee_resident_status, disposition_under_18,
            window_clearance_flag, ucr_offense_codes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        segment,
        to_str(line[2:4]),           # state_code
        to_str(line[4:13]),          # ori
        to_str(line[13:25]),         # incident_number
        to_date(line[25:33]),        # incident_date
        to_int(line[33:35]),         # arrestee_sequence_number
        to_str(line[35:47]),         # arrest_transaction_number
        to_date(line[47:55]),        # arrest_date
        to_str(line[55:56]),         # arrest_type
        to_str(line[56:57]),         # multiple_arrestee_indicator
        to_str(line[57:60]),         # ucr_arrest_offense_code
        to_str(line[66:68]),         # arrestee_age
        to_str(line[68:69]),         # arrestee_sex
        to_str(line[69:70]),         # arrestee_race
        to_str(line[70:71]),         # arrestee_ethnicity
        to_str(line[71:72]),         # arrestee_resident_status
        to_str(line[72:73]),         # disposition_under_18
        to_str(line[73:74]) if segment == 'W6' else None,  # window_clearance_flag
        extract_repeating_field(line, 74, 3, 10) if segment == 'W6' else None  # ucr_offense_codes for W6
    ))
    
    arrestee_id = cursor.lastrowid
    
    # Extract weapons (2 weapons, 3 chars each)
    weapons = []
    for i in range(2):
        pos = 60 + (i * 3)
        weapon_code = to_str(line[pos:pos + 2])
        auto_indicator = to_str(line[pos + 2:pos + 3])
        if weapon_code:
            weapons.append((arrestee_id, i + 1, weapon_code, auto_indicator))
    
    if weapons:
        cursor.executemany("""
            INSERT INTO arrestee_weapons (arrestee_id, weapon_sequence, weapon_code, automatic_indicator)
            VALUES (%s, %s, %s, %s)
        """, weapons)

def process_group_b_arrest(line, cursor):
    # Process 07 records
    cursor.execute("""
        INSERT INTO group_b_arrest (
            state_code, ori, arrest_transaction_number, arrest_date, arrestee_sequence_number,
            city_submission, arrest_type, ucr_group_b_code, arrestee_age, arrestee_sex,
            arrestee_race, arrestee_ethnicity, arrestee_resident_status, disposition_under_18
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        to_str(line[2:4]),           # state_code
        to_str(line[4:13]),          # ori
        to_str(line[13:25]),         # arrest_transaction_number
        to_date(line[25:33]),        # arrest_date
        to_int(line[33:35]),         # arrestee_sequence_number
        to_str(line[35:39]),         # city_submission
        to_str(line[39:40]),         # arrest_type
        to_str(line[40:43]),         # ucr_group_b_code
        to_str(line[49:51]),         # arrestee_age
        to_str(line[51:52]),         # arrestee_sex
        to_str(line[52:53]),         # arrestee_race
        to_str(line[53:54]),         # arrestee_ethnicity
        to_str(line[54:55]),         # arrestee_resident_status
        to_str(line[55:56])          # disposition_under_18
    ))
    
    arrest_id = cursor.lastrowid
    
    # Extract weapons (2 weapons, 3 chars each)
    weapons = []
    for i in range(2):
        pos = 43 + (i * 3)
        weapon_code = to_str(line[pos:pos + 2])
        auto_indicator = to_str(line[pos + 2:pos + 3])
        if weapon_code:
            weapons.append((arrest_id, i + 1, weapon_code, auto_indicator))
    
    if weapons:
        cursor.executemany("""
            INSERT INTO group_b_weapons (group_b_arrest_id, weapon_sequence, weapon_code, automatic_indicator)
            VALUES (%s, %s, %s, %s)
        """, weapons)


# Import function
def import_nibrs_data(filename, max_lines=None):
    """
    Import NIBRS data from file
    
    Args:
        filename: Path to NIBRS master file
        max_lines: Optional limit for testing (None = import all)
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    record_counts = {
        'BH': 0, 'B2': 0, 'B3': 0, '01': 0, 'W1': 0, '02': 0,
        '03': 0, 'W3': 0, '04': 0, '05': 0, '06': 0, 'W6': 0, '07': 0,
        'errors': 0, 'unknown': 0
    }
    
    processed_lines = 0
    bytes_read = 0
    commit_interval = 10000

    total_bytes = os.path.getsize(filename)
    start_time = time.time()
    last_progress_time = start_time
    last_progress_bytes = 0

    batch_header_cache = {}
    
    print("="*80)
    print("NIBRS DATA IMPORT")
    print("="*80)
    print(f"File: {filename}")
    print(f"File size: {format_bytes(total_bytes)}")
    if max_lines:
        print(f"Test mode: first {max_lines:,} lines only")
    print("="*80)
    
    try:
        with open(filename, "r", encoding="ascii", errors="ignore") as f:
            for line in f:
                processed_lines += 1
                bytes_read += len(line.encode("ascii", errors="ignore"))
                
                if processed_lines % 100000 == 0:
                    now = time.time()
                    elapsed_total = now - start_time
                    elapsed_since_last = now - last_progress_time
                    bytes_since_last = bytes_read - last_progress_bytes

                    pct_done = bytes_read / total_bytes * 100
                    bytes_remaining = total_bytes - bytes_read
                    speed_bps = bytes_since_last / elapsed_since_last if elapsed_since_last > 0 else 0
                    eta_seconds = bytes_remaining / speed_bps if speed_bps > 0 else 0
                    avg_speed = bytes_read / elapsed_total if elapsed_total > 0 else 0

                    print(
                        f"  {pct_done:5.1f}%  |  "
                        f"{format_bytes(bytes_read)} / {format_bytes(total_bytes)}  |  "
                        f"{processed_lines:,} lines  |  "
                        f"speed: {format_bytes(int(avg_speed))}/s  |  "
                        f"ETA: {format_eta(eta_seconds)}"
                    )

                    last_progress_time = now
                    last_progress_bytes = bytes_read
                
                if max_lines and processed_lines > max_lines:
                    break
                
                if len(line) < 2:
                    continue
                
                segment = line[0:2]
                
                try:
                    if segment in ['BH', 'B2', 'B3']:
                        process_batch_header(line, cursor, batch_header_cache)
                        record_counts[segment] += 1
                    
                    elif segment in ['01', 'W1']:
                        process_incident(line, cursor)
                        record_counts[segment] += 1
                    
                    elif segment == '02':
                        process_offense(line, cursor)
                        record_counts['02'] += 1
                    
                    elif segment in ['03', 'W3']:
                        process_property(line, cursor)
                        record_counts[segment] += 1
                    
                    elif segment == '04':
                        process_victim(line, cursor)
                        record_counts['04'] += 1
                    
                    elif segment == '05':
                        process_offender(line, cursor)
                        record_counts['05'] += 1
                    
                    elif segment in ['06', 'W6']:
                        process_arrestee(line, cursor)
                        record_counts[segment] += 1
                    
                    elif segment == '07':
                        process_group_b_arrest(line, cursor)
                        record_counts['07'] += 1
                    
                    else:
                        record_counts['unknown'] += 1
                    
                    if processed_lines % commit_interval == 0:
                        conn.commit()
                
                except Exception as e:
                    print(f"\nError on line {processed_lines}, segment '{segment}': {str(e)}")
                    record_counts['errors'] += 1
                    continue
        
        conn.commit()
        
        print("\nInserting monthly activity data...")
        monthly_data = []
        month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        
        for cache_key, cache_data in batch_header_cache.items():
            batch_id = cache_data['id']
            for activity in cache_data['monthly_activities']:
                monthly_data.append((
                    batch_id,
                    activity['month'],
                    month_names[activity['month'] - 1],
                    activity['zero_report'],
                    activity['group_ab'],
                    activity['window']
                ))
        
        if monthly_data:
            cursor.executemany("""
                INSERT INTO batch_header_monthly_activity 
                (batch_header_id, month_number, month_name, zero_report_submitted, 
                 group_ab_submitted, window_record_submitted)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, monthly_data)
            conn.commit()
        
        total_elapsed = time.time() - start_time

        print("\n" + "="*80)
        print("IMPORT COMPLETED SUCCESSFULLY")
        print("="*80)
        print(f"Total lines processed: {processed_lines:,}")
        print(f"Total bytes read:      {format_bytes(bytes_read)}")
        print(f"Total time:            {format_eta(total_elapsed)}")
        print(f"Average speed:         {format_bytes(int(bytes_read / total_elapsed))}/s")
        print("\nRecord counts:")
        print(f"  Batch Headers (BH):    {record_counts['BH']:,}")
        print(f"  Batch B2:              {record_counts['B2']:,}")
        print(f"  Batch B3:              {record_counts['B3']:,}")
        print(f"  Incidents (01):        {record_counts['01']:,}")
        print(f"  Window Incidents (W1): {record_counts['W1']:,}")
        print(f"  Offenses (02):         {record_counts['02']:,}")
        print(f"  Property (03):         {record_counts['03']:,}")
        print(f"  Window Property (W3):  {record_counts['W3']:,}")
        print(f"  Victims (04):          {record_counts['04']:,}")
        print(f"  Offenders (05):        {record_counts['05']:,}")
        print(f"  Arrestees (06):        {record_counts['06']:,}")
        print(f"  Window Arrestees (W6): {record_counts['W6']:,}")
        print(f"  Group B Arrests (07):  {record_counts['07']:,}")
        print(f"\nErrors:                  {record_counts['errors']:,}")
        print(f"Unknown segments:        {record_counts['unknown']:,}")
        print("="*80)
        
    except Exception as e:
        print(f"\nFATAL ERROR: {str(e)}")
        print("Rolling back transaction...")
        conn.rollback()
        raise
    
    finally:
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")


# Entry point
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Import NIBRS data into MySQL')
    parser.add_argument('filename', help='Path to NIBRS master file')
    parser.add_argument('--test', type=int, metavar='N', 
                       help='Test mode: only import first N lines')
    
    args = parser.parse_args()
    
    import_nibrs_data(args.filename, max_lines=args.test)
