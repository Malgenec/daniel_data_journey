# Crime analysis: USA FBI 2020
Power BI Analytical Project for the Vilnius Coding School

<img width="1655" height="956" alt="image" src="https://github.com/user-attachments/assets/e2de1aac-3dc4-497b-8568-6af4aac9785d" />

[Check Full PDF Report](./Daniel_Garifulin_Project.pdf)

<br />
<br />

## Project Overview
This Project analyzes 7.9M crime incidents, 8.9M victims, and 2.2M arrests based on FBI 2020 public data.

Data source - official US website https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads

<details>
  <summary>Small glimpse at the original txt master file (4 GB, I'm showing only 40 lines)</summary>

['BH50AK0010100000000000000                ANCHORAGE                     AK1C941Y         3030020A         00028638800  39000000000000000000      000000000000000000      000000000000000000      000000000000000000      000000000  002020NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN020            \n']
['BH50AK0010200000000000000        20210101FAIRBANKS                     AK4 941Y         3030020AA        00003083200 258000000000000000000      000000000000000000      000000000000000000      000000000000000000      00000000006112020NYNNYNNYNNNNNYNNYNNYNNYNNYNNYNNYNNYN090            \n']
['0150AK0010200C60BROS9728N20201231R00010010100    N                                      N\n']
['0250AK0010200C60BROS9728N2020123111ACA  20   N  40       88\n']
['0450AK0010200C60BROS9728N2020123100111A                           I24FINN     M    01OK                                                \n']
['0550AK0010200C60BROS9728N202012310142MBN\n']
['0150AK0010200CE0BAARR728N20200819R00010010200    N                                      N\n']
['0250AK0010200CE0BAARR728N2020081911BCN  20   N  99       88\n']
['0450AK0010200CE0BAARR728N2020081900111B                           I03MBNN     N    01BE02BE                                            \n']
['0550AK0010200CE0BAARR728N202008190112MBN\n']
['0550AK0010200CE0BAARR728N202008190241MBN\n']
['0150AK0010200CE0BIBTR728N20201120R00010010100    N                                      N\n']
['0250AK0010200CE0BIBTR728N2020112013BCN  20   N  40       88\n']
['0450AK0010200CE0BIBTR728N2020112000113B                           I40MWNR     M    01BG                                                \n']
['0550AK0010200CE0BIBTR728N202011200132FWU\n']
['0150AK0010200CN0BABTL728N20201101R00010010100    N                                      N\n']
['0250AK0010200CN0BABTL728N20201101220CN  1901F            88\n']
['0350AK0010200CN0BABTL728N20201101716000005000                                                         \n']
['0450AK0010200CN0BABTL728N20201101001220                           I31FBNR                                                              \n']
['0550AK0010200CN0BABTL728N2020110100     \n']
['0150AK0010200CN0BAETM728N20200804R00010010100    N                                      N\n']
['0250AK0010200CN0BAETM728N2020080423GCN  23               88\n']
['0350AK0010200CN0BAETM728N20200804738000000650                                                         \n']
['0450AK0010200CN0BAETM728N2020080400123G                           I51FANR                                                              \n']
['0550AK0010200CN0BAETM728N2020080400     \n']
['0150AK0010200CN0BAFBV728N20200621R00010010100    N                                      N\n']
['0250AK0010200CN0BAFBV728N2020062123FCN  18               88\n']
['0350AK0010200CN0BAFBV728N20200621725000000070                                                         \n']
['0350AK0010200CN0BAFBV728N20200621765000000000                                                         \n']
['0450AK0010200CN0BAFBV728N2020062100123F                           I38FWNN          01RU                                                \n']
['0550AK0010200CN0BAFBV728N202006210100FUU\n']
['0150AK0010200CN0BAVBV728N20201101R14010010100    N                                      N\n']
['0250AK0010200CN0BAVBV728N20201101220CN  20  N            88\n']
['0350AK0010200CN0BAVBV728N20201101706000001183                                                         \n']
['0450AK0010200CN0BAVBV728N20201101001220                           I22MBNR                                                              \n']
['0550AK0010200CN0BAVBV728N2020110100     \n']
['0150AK0010200CN0BICRC728N20200801R00010010100    N                                      N\n']
['0250AK0010200CN0BICRC728N2020080113ACN  20   N  40       88\n']
['0450AK0010200CN0BICRC728N2020080100113A                           I16FWNR06   I    01BG                                                \n']
</details>

To "decrypt" the data, I've started with reading NIBRS record description pdf file, which consisted of 99 pages (sadly enough, this file was some sort of a scanned copy, so AI couldn't really help with making my work faster, and kept hallucinating).

Links to the [Python code that does decryption and extraction](https://github.com/Malgenec/daniel_data_journey/blob/main/power_bi_projects/crime_analysis/data_to_sql.py)
and [instructions how to use it](https://github.com/Malgenec/daniel_data_journey/blob/main/power_bi_projects/crime_analysis/data_to_sql_readme.md)

<br />
<br />

The project goal was to:

* Fulfill the project criteria provided by Vilnius Coding School
<details>
<summary>(Project criteria in Lithuanian)</summary>

|Nr.|Tema                                      |Aprašymas                                                                                     |Balai|Pavyzdys                                                                            |
|:-:|:----------------------------------------:|:--------------------------------------------------------------------------------------------:|:---:|:----------------------------------------------------------------------------------:|
|1  |Duomenų šaltinio pasirinkimas             |Pasirinktas įdomus, pakankamai didelis (>5000 eilučių) duomenų rinkinys su keliomis lentelėmis|5    |Kaggle rinkinys apie pardavimus, kuriame yra lentelės: Orders, Customers, Products  |
|2  |Duomenų transformacija ir valymas         |Tipų keitimas, trūkstamų reikšmių tvarkymas, nereikalingų stulpelių šalinimas                 |7    |Pašalinti tušti stulpeliai, konvertuoti datos formatai, užpildytos tuščios reikšmės |
|3  |Faktų ir dimensijų struktūra (STAR schema)|Sukurtos aiškios sąsajos tarp lentelių, identifikuoti raktai, schema pagrįsta modeliavimu     |7    |Sukurta Orders (faktų) lentelė su saitais į Products, Customers (dimensijų) lenteles|
|4  |Hierarchijos sukūrimas                    |Sukurtos naudotojo hierarchijos dimensijose                                                   |3    |Data: Metai > Ketvirtis > Mėnuo; Vieta: Šalis > Miestas                             |
|5  |Bazinių DAX formulių panaudojimas         |Sukurti bent 5 baziniai KPI (suma, vidurkis, skaičius)                                        |5    |Total Sales = SUM(Orders[Amount]); Customer Count = DISTINCTCOUNT(Customers[ID])    |
|6  |Advanced DAX: Time intelligence           |Pritaikytos bent 3 pažangios formulės: YTD, YOY, filtruoti kontekstai                         |6    |Sales YTD = TOTALYTD(SUM(Orders[Amount]), 'Date'[Date])                             |
|7  |Rodiklių lentelė ir grupavimas            |Visi KPI įkelti į atskirą lentelę, matų grupavimas į aplankus                                 |4    |„KPI Metrics“ lentelė su aplankais: Sales, Customers, Time Analysis                 |
|8  |Ataskaitos dizaino tema                   |Parinkta ar susikurta Power BI tema su vientisu dizainu                                       |5    |Naudojama švelni žalsva tema su vientisais šriftais ir spalvomis                    |
|9  |Estetika                                  |Aiškus pavadinimai, išlygiuoti objektai, suprantamos spalvos                                  |5    |KPI su pavadinimais „Pardavimai šiemet“, „Augimas %“, švarus layout                 |
|10 |Pagrindinis dashboard’as                  |Aiškiai atvaizduoti svarbiausi KPI, skaidrūs filtrai, pagrindinė analizė                      |10   |Pardavimų augimo pagal metus ir klientų tipą vizualizacija                          |
|11 |Papildomas dashboard’as                   |Detalesnė analizė pagal pasirinktą dimensiją (pvz., produktus, šalis)                         |10   |Produktų kategorijų pelningumo analizė                                              |
|12 |Drillthrough                              |Galimybė eiti į detalesnį puslapį                                                             |5    |Iš kategorijų į vieno produkto puslapį                                              |
|13 |Papildomas puslapis: klausimai ir įžvalgos|Atsakyti į analizės pradžioje keltus klausimus, pateiktos įžvalgos                            |5    |"Ar klientų lojalumas susijęs su grąžinimų skaičiumi?" ir pan.                      |
|14 |Bookmark’ai                               |Sukurtos žymės valdyti filtravimą, rodinius ar perėjimus                                      |5    |„Išvalyti filtrus“ mygtukas, „Rodinių perjungimas“                                  |
|   |                                          |                                                                                              |     |                                                                                    |
</details>

* Build a clean star schema from messy raw datasets

* Normalize crime statistics by population

* Identify structural crime patterns

* Separate emotional assumptions from data-driven conclusions

The project focuses on analytical modeling quality, not dashboard decoration.

Since some criteria required to show Power BI skills, data was not modified in MySQL (though it would be much easier).

Model schema:
<img width="1785" height="915" alt="image" src="https://github.com/user-attachments/assets/8c979f86-1d9e-4edc-817b-d2950d20277a" />

<br />
<br />

## Key Metrics
* Total Incidents: 7.92M

* Total Arrests: 2.19M

* Violent Crime Share: 24%

* Arrest Rate (per 100k population): 655

* Hate Crimes: 5,994 (≈0.1% of all crimes)

<br />
<br />

## Main Insights

### 1. Crime Structure (National Level)
Top 3 offense categories:
* Drug/Narcotic Violations (~30%)

* Simple Assault (~22%)

* Drug Equipment Violations (~15%)
Crime is highly concentrated in a limited number of categories.

<br />
<br />

### 2. Age Impact
* Most arrested group: 20–29 years

* 17.4% over-representation compared to population share

* 50+ group strongly under-represented

**Age is a stronger predictor than race.**

<br />
<br />

### 3. Gender Distribution

* 72% of arrestees are male

* Male over-representation: +23%

* Victim split: ~51% female / 49% male

**Sex has stronger statistical skew than race.**

<br />
<br />

### 4. Representation Analysis (Population-Adjusted)

Representation = (arrest share %) − (population share %)

**Findings:**

* Black race: +18.5% over-representation

* Male sex: +23.3% over-representation

* Young adults: +17.4% over-representation

**Conclusion:**
Single-variable analysis (race only) is statistically incomplete.
Socioeconomic factors are not included in the dataset.

<br />
<br />

### 5. Hate Crime Patterns

* ~6,000 hate crimes nationwide

* Highest per-capita rate: Vermont

* Most targeted group: Black race (35.2%)

**Hate crimes represent a small fraction of total crime but disproportionately affect minority groups.**

<br />
<br />

## Data Modeling & Architecture

Raw data was poorly structured and required significant transformation.

### Modeling Approach

* Designed Star Schema

* Separated fact tables (incidents, arrests, victims)

* Created surrogate keys

* Population normalization for fair comparison

* Built representation metrics in DAX

### Model includes:

* Fact tables for arrests, offenses, victims

* Dimensions for date, state, city, race, age, bias, relationship, offense type

* Population-adjusted measures

* Many-to-many relationship handled through bridge table

<br />
<br />

## Analytical Questions Answered

Which state had the highest incident count?

Which crimes dominate nationally?

When is crime activity seasonally lower?

Are young people more likely to be arrested?

Are stereotypes supported by normalized data?

How significant are hate crimes relative to total crime?

<br />
<br />

## What This Project Demonstrates

* Ability to structure messy raw data

* Understanding of dimensional modeling

* Statistical normalization (per 100k population)

* Analytical reasoning beyond surface-level metrics

* Ability to separate correlation from emotional bias

* Business-style interpretation of public data

<br />
<br />

## Notes

Some small race categories were excluded from certain visuals due to Power BI rendering limitations.

Dataset does not include socioeconomic variables (poverty, urbanization, education), limiting causal interpretation.

<br />
<br />

## Author

Daniel Garifulin
