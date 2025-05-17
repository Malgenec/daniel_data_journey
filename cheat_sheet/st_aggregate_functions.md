## `COUNT` function

`COUNT` function lets you count rows of data to output it as a number.
If the column is specified, it counts only non-NULL data (NULL data is skipped).

```
SELECT COUNT(*) FROM REAGENTS;
```
:star: Output:

|count|
|:---:|
|16   |

## `MIN` and `MAX` functions

`MIN` function outputs the smallest value of the given column.

```
SELECT MIN(Quantity) FROM Reagents;
```
:star: Output:

|min|
|:-:|
|2  |

`MAX` function outputs the biggest value of the given column.

```
SELECT * FROM Reagents
WHERE Quantity = (SELECT MAX(Quantity) FROM Reagents);
```
|Name   |Concentration|Quantity|Manufacturer|
|:-----:|:-----------:|:------:|:----------:|
|Uranium|100          |9001    |Neighbour   |

## `AVG` function

`AVG` function outputs the average value of the given column.

```
SELECT AVG(Concentration) FROM Reagents
WHERE Name LIKE '%Acid%';
```
:star: Output:

|Avg                |
|:-----------------:|
|44.2500000000000000|

## `SUM` function

`SUM` calculates the sum of the given column values.

```
SELECT SUM(Quantity) FROM Reagents
WHERE Manufacturer = 'Neighbour';
```
:star: Output:

|Sum |
|:--:|
|9645|

## `GROUP BY` function

When you need to group up rows, for example with the same value, `GROUP BY` does that.
For example you need to calculate the amount of reagent types bought from different manufacturers:

```
SELECT Manufacturer, COUNT(Name) AS Reagent_Types
FROM Reagents
GROUP BY Manufacturer;
```
:star: Output:

|Manufacturer |Reagent_types|
|:-----------:|:-----------:|
|Neighbour    |4            |
|Sigma-Aldrich|7            |
|LabSource    |2            |
|Mother Earth |2            |
|EarthWorks   |1            |

## `HAVING` function

`HAVING` function does similar job as `WHERE`, except that it's used for additional data filtering after `GROUP BY`.
For example, we need to find manufacturers that supply 2 or more reagents with concentration over 50 (why not?)
```
SELECT Manufacturer, COUNT(*) AS High_Concentration_Reagents
FROM Reagents
WHERE Concentration >= 50
GROUP BY Manufacturer
HAVING COUNT(*) >= 2;
```
:star: Output:

|Manufacturer |High_concentration_reagents|
|:-----------:|:-------------------------:|
|Sigma-Aldrich|2                          |
|Neighbour    |4                          |
|Mother Earth |2                          |
