# Statement WHERE

WHERE is used to specify conditions in a query.

There are different operators used in a WHERE clause:

## Standard Numerical Operators:

### **=** - equal

### **!=** - not equal

### **<, <=, >, >=** - less/less or equal/more/more or equal to

## Logical Operators:

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

This would show only the rows containing 10 or 50 in the Concentration column.

### NOT Operator

NOT operator reverts the condition, for example:

```
SELECT * FROM Reagents
WHERE Manufacturer NOT IN ('Neighbour', 'Mother Earth');
```

Would select us rows where Manufacturer column value is not equal to 'Neighbour' or 'Mother Earth'.
"Nitric Acid"	68	13	"Sigma-Aldrich"
"Sulfuric Acid"	32	2	"Sigma-Aldrich"
"Phosphoric Acid"	40	34	"Sigma-Aldrich"
"Hydrochloric Acid"	37	10	"Sigma-Aldrich"
"Potassium Iodide"	5	25	"LabSource"
"Sodium Hydroxide"	50	100	"Sigma-Aldrich"
"Ammonium Nitrate"	60	300	"LabSource"
"Copper Sulfate"	20	150	"Sigma-Aldrich"
"Calcium Carbonate"	80	200	"EarthWorks"
"Phenolphthalein"	1	5	"Sigma-Aldrich"
