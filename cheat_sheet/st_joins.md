Join statements are needed to manipulate data between several tables. There are several types

### INNER JOIN statement
With the help of JOIN we can get data from 2 different tables which have a common key.
The result is a row containing all the data from those 2 tables.
The way INNER JOIN works is that it matches the data from the first table with the second one:

```
SELECT table1_column1, table2_column1
FROM table1
INNER JOIN table2
  ON table1.id = table2.id
...
;
```

### LEFT JOIN, RIGHT JOIN statements

