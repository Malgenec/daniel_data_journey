#This script is used to transform the result of SQL query into a beautiful GitHub table.

#NOTE that it will require you to paste -> enter (to confirm that you paste it as multi-line) -> enter (to enter your input) -> enter (to end your input, since it needs a way to understand that your multi-line ended)

#Example of SQL query copy-paste result: 
"""
"name"	"concentration"	"quantity"	"manufacturer"
"Nitric Acid"	68	13	"Sigma-Aldrich"
"Ethanol"	50	69	"Neighbour"
"NaCl"	100	454	"Mother Earth"
"Sulfuric Acid"	32	2	"Sigma-Aldrich"
"Phosphoric Acid"	40	34	"Sigma-Aldrich"
"Uranium"	100	9001	"Neighbour"
"Hydrochloric Acid"	37	10	"Sigma-Aldrich"
"Potassium Iodide"	5	25	"LabSource"
"Sodium Hydroxide"	50	100	"Sigma-Aldrich"
"Methanol"	99	500	"Neighbour"
"Acetone"	100	250	"Mother Earth"
"Ammonium Nitrate"	60	300	"LabSource"
"Copper Sulfate"	20	150	"Sigma-Aldrich"
"Zinc Powder"	95	75	"Neighbour"
"Calcium Carbonate"	80	200	"EarthWorks"
"Phenolphthalein"	1	5	"Sigma-Aldrich"
"""

SQL_result=[]
print("Insert the SQL query result (with headers): ")

#The following loop will read the input if you copy as different sentences.
while True:
    try:
        line_input = input('')
        if line_input=="":
            break
    except EOFError:
        break
    SQL_result.append(line_input.replace('"','')) #ACHTUNG! Removes ALL THE quotes, even if original data has them.

SQL_result = [line.split("\t") for line in SQL_result if line.strip() != ""] #Split each line by tab and remove empty ones

#Format the table so all the elements are the same length
max_lengths = [max(len(str(item)) for item in column) for column in zip(*SQL_result)] #Define the longest element's char number in each column
for line in SQL_result:
    column_counter = 0 #Counter to loop through the columns
    for element_number in range(len(line)):
        if len(line[element_number]) < max_lengths[column_counter]:
            line[element_number] = line[element_number].ljust(max_lengths[column_counter]) #Adds spaces to the right of the element
        column_counter += 1

HeaderUnderline = []
for i in range(len(SQL_result[0])):
    HeaderUnderline.append('-' * (max_lengths[i]-2)) #Create the underline for the header

#Print each element in a borders
for value in SQL_result:
    print('|'+'|'.join(value)+'|') #Borders the elements with | and prints them
    if value == SQL_result[0]:
        print('|:' + ':|:'.join(HeaderUnderline) + ':|') #Prints the "alignment row" after the header
