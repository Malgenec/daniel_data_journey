# Statement WHERE

WHERE is used to specify conditions in a query.

There are different operators used in a WHERE clause:

## Standard Numerical Operators:

### **<, <=** - less, less or equal to
### **>, >=** - more, more or equal to

## Logical Operators:

### **=** - equal

### **!=** or **<>**- not equal

### AND Operator

AND is used to combine two or more conditions. This returns values only where all the conditions were met.

### OR Operator

OR is used to combine multiple conditions, and returns values where at least one of the conditions were met.

### IN Operator

IN returns values that matches any item in the list. For example:

```
SELECT * FROM Reagents
WHERE Concentration in (10,50);
```

This would show only the rows containing 10 or 50 in the Concentration column:

|Name            |Concentration|Quantity|Manufacturer |
|:--------------:|:-----------:|:------:|:-----------:|
|Ethanol         |50           |69      |Neighbour    |
|Sodium Hydroxide|50           |100     |Sigma-Aldrich|

### BETWEEN Operator

BETWEEN returns rows which would have a value between two values in a statement (alphabetically or in a number range). You also need to use "AND" statement between the two values.

For example if you would like to show the values that alphabetically are between Copper Sulfate and NaCl (shelf-sorting?), you would use it like this<sup>*</sup>:

```
SELECT * FROM Reagents
WHERE Name BETWEEN 'Copper Sulfate' AND 'NaCl';
```

|Name             |Concentration|Quantity|Manufacturer |
|:---------------:|:-----------:|:------:|:-----------:|
|Ethanol          |50           |69      |Neighbour    |
|NaCl             |100          |454     |Mother Earth |
|Hydrochloric Acid|37           |10      |Sigma-Aldrich|
|Methanol         |99           |500     |Neighbour    |
|Copper Sulfate   |20           |150     |Sigma-Aldrich|

*_Note that the values are sorted by the table original row order, rather than alphabetically. ORDER BY Name is what you're looking for if you want them sorted out._

### NOT Operator

NOT operator reverts the condition, for example:

```
SELECT * FROM Reagents
WHERE Manufacturer NOT IN ('Neighbour', 'Mother Earth');
```

Would select us rows where Manufacturer column value is not equal to 'Neighbour' or 'Mother Earth':

|Name             |Concentration|Quantity|Manufacturer |
|:---------------:|:-----------:|:------:|:-----------:|
|Nitric Acid      |68           |13      |Sigma-Aldrich|
|Sulfuric Acid    |32           |2       |Sigma-Aldrich|
|Phosphoric Acid  |40           |34      |Sigma-Aldrich|
|Hydrochloric Acid|37           |10      |Sigma-Aldrich|
|Potassium Iodide |5            |25      |LabSource    |
|Sodium Hydroxide |50           |100     |Sigma-Aldrich|l
|Ammonium Nitrate |60           |300     |LabSource    |
|Copper Sulfate   |20           |150     |Sigma-Aldrich|
|Calcium Carbonate|80           |200     |EarthWorks   |
|Phenolphthalein  |1            |5       |Sigma-Aldrich|

### LIKE Operator

LIKE Operator is a text, case insensitive operator which compares given string with the values in the table and returns rows having this string.
Without special characters it's the same as '=' but slower. **Wildcards** is where LIKE shines.

#### % Wildcard 

This wildcard is used for any number of missing (or not) characters, can be placed in any string part. For example, if you want the reagent name to contain 'nol', you could write:

```
SELECT * FROM Reagents
WHERE Name LIKE '%nol%';
```

|Name           |Concentration|Quantity|Manufacturer |
|:-------------:|:-----------:|:------:|:-----------:|
|Ethanol        |50           |69      |Neighbour    |
|Methanol       |99           |500     |Neighbour    |
|Phenolphthalein|1            |5       |Sigma-Aldrich|

Now if you would want to see some basic alcohols which just end with 'nol':

```
SELECT * FROM Reagents
WHERE Name LIKE '%nol';
```

|Name    |Concentration|Quantity|Manufacturer|
|:------:|:-----------:|:------:|:----------:|
|Ethanol |50           |69      |Neighbour   |
|Methanol|99           |500     |Neighbour   |

As you can see, wildcard % was used to the left of the string, so it matches with every string ending with 'nol', but not when 'nol' is in the middle like 'PheNOLphthalein'. Writing 'meow%' would match with the strings starting with 'meow'.

#### _ Wildcard

_ Wildcard represents a ~~hangman game ~~ single missing character. For example:

```
SELECT * FROM Reagents
WHERE Name LIKE 'N_C_';
```

|Name|Concentration|Quantity|Manufacturer|
|:--:|:-----------:|:------:|:----------:|
|NaCl|100          |454     |Mother Earth|
