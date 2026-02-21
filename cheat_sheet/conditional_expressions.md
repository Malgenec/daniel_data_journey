### CASE WHEN

CASE conditional expression is used for example when we want to 'group' our data into some categories.
Syntax:
```
CASE
WHEN <expression> THEN <result>
WHEN <expression2> THEN <result2>
...
ELSE <another result when other conditions weren't met>
END AS <column name>
```

For example, in our reagents data I would like to group all the acids as "Acids", reagents which end with "ol" as "Alcohols", and the rest as "Other".

```
SELECT Name,

CASE
WHEN Name LIKE "%Acid%" THEN "Acids"
WHEN Name LIKE "%ol" THEN "Alcohols"
ELSE "Other"
END AS Category

FROM Reagents;
```
Result:
|Name             |Category     |
|:---------------:|:-----------:|
|Phenolphthalein  |Other        |
|Sulfuric Acid    |Acid         |
|Phosphoric Acid  |Acid         |
|Hydrochloric Acid|Acid         |
|Sodium Hydroxide |Other        |
|Copper Sulfate   |Other        |
|Nitric Acid      |Acid         |
|Zinc Powder      |Other        |
|Uranium          |Other        |
|Methanol         |Alcohols     |
|Ethanol          |Alcohols     |
|NaCl             |Other        |
|Acetone          |Other        |
|Potassium Iodide |Other        |
|Ammonium Nitrate |Other        |
|Calcium Carbonate|Other        |

### COALESCE and CAST

Consider we have the following table:
|Name             |Concentration|Quantity|Volume|Manufacturer |
|:---------------:|:-----------:|:------:|:----:|:-----------:|
|Nitric Acid      |68           |13      |1     |Sigma-Aldrich|
|Ethanol          |50           |69      |5     |Neighbour    |
|NaCl             |100          |454     |null  |Mother Earth |
|Sulfuric Acid    |32           |2       |1     |Sigma-Aldrich|
|Phosphoric Acid  |40           |34      |1     |Sigma-Aldrich|
|Uranium          |100          |9001    |null  |Neighbour    |
|Hydrochloric Acid|37           |10      |2     |Sigma-Aldrich|
|Potassium Iodide |5            |25      |null  |LabSource    |
|Sodium Hydroxide |50           |100     |null  |Sigma-Aldrich|
|Methanol         |99           |500     |1     |Neighbour    |
|Acetone          |100          |250     |5     |Mother Earth |
|Ammonium Nitrate |60           |300     |1     |LabSource    |
|Copper Sulfate   |20           |150     |1     |Sigma-Aldrich|
|Zinc Powder      |95           |75      |null  |Neighbour    |
|Calcium Carbonate|80           |200     |null  |EarthWorks   |
|Phenolphthalein  |1            |5       |1     |Sigma-Aldrich|

We have volumes added to our table, and if it's not liquid there is a null value. But we want to calculate the overall volume of the liquids we have, and if the reagent is solid - fill "Solid".

Here comes COALESCE and CAST to help us.

COALESCE checks the value, and if it's null - it places default value.

```
SELECT COALESCE (column, default_value_if_null)
FROM table;
```

CAST might help us further - it converts type of the value to the desired. We can't have both integers and varchars in one column, but we can convert integers to varchars and have the whole column type being varchar.
```
CAST(value/column AS VARCHAR)
```
So let's apply both expressions:

```
SELECT Name,
COALESCE(CAST(Quantity*Volume AS VARCHAR),'Solid') AS Total_Volume
FROM Reagents;
```

Result:
|Name             |Total_Volume|
|:---------------:|:----------:|
|Nitric Acid      |13          |
|Ethanol          |345         |
|NaCl             |Solid       |
|Sulfuric Acid    |2           |
|Phosphoric Acid  |34          |
|Uranium          |Solid       |
|Hydrochloric Acid|20          |
|Potassium Iodide |Solid       |
|Sodium Hydroxide |Solid       |
|Methanol         |500         |
|Acetone          |1250        |
|Ammonium Nitrate |300         |
|Copper Sulfate   |150         |
|Zinc Powder      |Solid       |
|Calcium Carbonate|Solid       |
|Phenolphthalein  |5           |

### REPLACE

Another powerful function which under specific condition can modify values.

Syntax:
```
REPLACE(column, 'what_to_replace'. 'replace_to_this')
```

Simple example: we want to have "Acid" in lowercase like "acid". Let's do it:
```
SELECT
REPLACE(Name, 'Acid', 'acid')
FROM Reagents;
```

Will result in:

|Name             |
|:---------------:|
|Nitric acid      |
|Ethanol          |
|NaCl             |
|Sulfuric acid    |
|Phosphoric acid  |
|Uranium          |
|Hydrochloric acid|
|Potassium Iodide |
|Sodium Hydroxide |
|Methanol         |
|Acetone          |
|Ammonium Nitrate |
|Copper Sulfate   |
|Zinc Powder      |
|Calcium Carbonate|
|Phenolphthalein  |
