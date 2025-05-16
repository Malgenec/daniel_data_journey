## Table: North_american_cities

|City               |Country      |Population|Latitude |Longitude  |
|:-----------------:|:-----------:|:--------:|:-------:|:---------:|
|Guadalajara        |Mexico       |1500800   |20.659699|-103.349609|
|Toronto            |Canada       |2795060   |43.653226|-79.383184 |
|Houston            |United States|2195914   |29.760427|-95.369803 |
|New York           |United States|8405837   |40.712784|-74.005941 |
|Philadelphia       |United States|1553165   |39.952584|-75.165222 |
|Havana             |Cuba         |2106146   |23.05407 |-82.345189 |
|Mexico City        |Mexico       |8555500   |19.432608|-99.133208 |
|Phoenix            |United States|1513367   |33.448377|-112.074037|
|Los Angeles        |United States|3884307   |34.052234|-118.243685|
|Ecatepec de Morelos|Mexico       |1742000   |19.601841|-99.050674 |
|Montreal           |Canada       |1717767   |45.501689|-73.567256 |
|Chicago            |United States|2718782   |41.878114|-87.629798 |

### Task 1

List all the Canadian cities and their populations

```
SELECT City, Population FROM North_American_Cities
WHERE Country = Canada;
```

### Task 2

Order all the cities in the United States by their latitude from north to south

```
SELECT City FROM North_American_Cities
WHERE Country = 'United States'
ORDER BY Latitude DESC;
```

### Task 3

List all the cities west of Chicago, ordered from west to east

```
SELECT City FROM North_American_Cities
WHERE Longitude <
(SELECT Longitude FROM North_American_Cities WHERE City = 'Chicago') -- This finds Chicago's longitude
ORDER BY Longitude ASC;
```

### Task 4

List the two largest cities in Mexico (by population)

```
SELECT City FROM North_American_Cities
WHERE Country = 'Mexico'
ORDER BY Population DESC
LIMIT 2;
```

### Task 5

List the third and fourth largest cities (by population) in the United States and their population.

```
SELECT City, Population FROM North_American_Cities
WHERE Country = 'United States'
ORDER BY Population DESC
LIMIT 2 OFFSET 2;
/*We sort the cities in US by population in a descending
order, then offseting to 2 (to start from 3rd) and limiting
to 2 to find 3'rd and 4'th cities*/
```
