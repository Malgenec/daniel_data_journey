### ORDER BY statement

ORDER BY sorts out the output based on the request.
For example, if we would like to know which reagents are in the shortage and show all the reagents, we would write:

```
SELECT Name, Quantity FROM Reagents
ORDER BY Quantity;
```
|Name             |Quantity|
|:---------------:|:------:|
|Sulfuric Acid    |2       |
|Phenolphthalein  |5       |
|Hydrochloric Acid|10      |
|Nitric Acid      |13      |
|...              |...     |

This automatically sorts in an ascending order. To sort out a table in a descending order, we use DESC statement (ASC - ascending, DESC - descending). Let's try with string values:

```
SELECT Name, Manufacturer FROM Reagents
ORDER BY Manufacturer DESC;
```

|Name             |Manufacturer |
|:---------------:|:-----------:|
|Phenolphthalein  |Sigma-Aldrich|
|Sulfuric Acid    |Sigma-Aldrich|
|Phosphoric Acid  |Sigma-Aldrich|
|Hydrochloric Acid|Sigma-Aldrich|
|Sodium Hydroxide |Sigma-Aldrich|
|Copper Sulfate   |Sigma-Aldrich|
|Nitric Acid      |Sigma-Aldrich|
|Zinc Powder      |Neighbour    |
|Uranium          |Neighbour    |
|Methanol         |Neighbour    |
|Ethanol          |Neighbour    |
|NaCl             |Mother Earth |
|Acetone          |Mother Earth |
|Potassium Iodide |LabSource    |
|Ammonium Nitrate |LabSource    |
|Calcium Carbonate|EarthWorks   |

### DISTINCT statement

DISTINCT statement is used for non-duplicate values. The most simple example:

```
SELECT DISTINCT Manufacturer FROM Reagents;
```

|Manufacturer |
|:-----------:|
|Neighbour    |
|Sigma-Aldrich|
|LabSource    |
|Mother Earth |
|EarthWorks   |

### LIMIT and OFFSET statements

Those statements are used to specifically limit the amount of rows we'll get in our output.
It might be commonly used in catalog-like websites, when you see multiple pages with limited to some amount (like 50) items on a single page. Example:

```
SELECT * FROM Reagents
ORDER BY quantity
LIMIT 5 OFFSET 1;
```
|Name             |Concentration|Quantity|Manufacturer |
|:---------------:|:-----------:|:------:|:-----------:|
|Phenolphthalein  |1            |5       |Sigma-Aldrich|
|Hydrochloric Acid|37           |10      |Sigma-Aldrich|
|Nitric Acid      |68           |13      |Sigma-Aldrich|
|Potassium Iodide |5            |25      |LabSource    |
|Phosphoric Acid  |40           |34      |Sigma-Aldrich|

This way I've LIMITed rows to 5 and start after the first row (to skip it) with the OFFSET, to show the least by quantity reagents skipping the first one (which is weird, but that's my example).
