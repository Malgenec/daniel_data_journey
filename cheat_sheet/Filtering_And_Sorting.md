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
