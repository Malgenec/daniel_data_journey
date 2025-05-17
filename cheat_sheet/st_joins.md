Imagine we have another table containing data about suppliers:

### Table: Suppliers

|SupplierID  |Name            |Country    |ContactEmail                                                 |
|:----------:|:--------------:|:---------:|:-----------------------------------------------------------:|
|1           |Sigma-Aldritch  |USA        |[contact@sigma.com](mailto:contact@sigma.com)                |
|2           |Neighbour       |Lithuania  |[biggestdrunkard@gmail.com](mailto:biggestdrunkard@gmail.com)|
|3           |LabSource       |UK         |[contact@labsource.co.uk](mailto:contact@labsource.co.uk)    |
|4           |EarthWorks      |Australia  |[support@earthworks.au](mailto:support@earthworks.au)        |
|5           |Future Supplier |Latvia     |[futuresupplier@gmail.com](futuresupplier@gmail.com)         |

Join statements are needed to manipulate data between several tables. There are several types


## `INNER JOIN` statement
With the help of `JOIN` we can get data from 2 different tables which have a common key.
The result is a row containing all the data from those 2 tables, having this common key - declared with `ON` statement.

So we need to see reagents with their quantities, and the emails of suppliers to contact them (if they exist).

```
SELECT Reagents.Name, Quantity, ContactEmail
FROM Reagents
INNER JOIN Suppliers
  ON Reagents.Manufacturer = Suppliers.Name
```
<details>
<summary>:star:Output:</summary>
  
|Name             |Quantity|ContactEmail             |
|:---------------:|:------:|:-----------------------:|
|Nitric Acid      |13      |contact@sigma.com        |
|Ethanol          |69      |biggestdrunkard@gmail.com|
|Sulfuric Acid    |2       |contact@sigma.com        |
|Phosphoric Acid  |34      |contact@sigma.com        |
|Uranium          |9001    |biggestdrunkard@gmail.com|
|Hydrochloric Acid|10      |contact@sigma.com        |
|Potassium Iodide |25      |contact@labsource.co.uk  |
|Sodium Hydroxide |100     |contact@sigma.com        |
|Methanol         |500     |biggestdrunkard@gmail.com|
|Ammonium Nitrate |300     |contact@labsource.co.uk  |
|Copper Sulfate   |150     |contact@sigma.com        |
|Zinc Powder      |75      |biggestdrunkard@gmail.com|
|Calcium Carbonate|200     |support@earthworks.au    |
|Phenolphthalein  |5       |contact@sigma.com        |

</details>

There won't be reagents listed from Mother Earth as Mother Earth is not in the Suppliers table. There is also no Future Supplier email listed, because we don't have reagents from them yet.

## `LEFT JOIN` , `RIGHT JOIN` statements

`LEFT JOIN` leaves all data from the left table and joins data from the right table with the key. There will be empty data in the right table columns if there is no match:

```
SELECT Reagents.Name, Quantity, ContactEmail
FROM Reagents
LEFT JOIN Suppliers
  ON Reagents.Manufacturer = Suppliers.Name;
```
<details>
<summary>:star:Output:</summary>
  
|Name             |Quantity|ContactEmail             |
|:---------------:|:------:|:-----------------------:|
|Nitric Acid      |13      |contact@sigma.com        |
|Ethanol          |69      |biggestdrunkard@gmail.com|
|NaCl             |454     |                         |
|Sulfuric Acid    |2       |contact@sigma.com        |
|Phosphoric Acid  |34      |contact@sigma.com        |
|Uranium          |9001    |biggestdrunkard@gmail.com|
|Hydrochloric Acid|10      |contact@sigma.com        |
|Potassium Iodide |25      |contact@labsource.co.uk  |
|Sodium Hydroxide |100     |contact@sigma.com        |
|Methanol         |500     |biggestdrunkard@gmail.com|
|Acetone          |250     |                         |
|Ammonium Nitrate |300     |contact@labsource.co.uk  |
|Copper Sulfate   |150     |contact@sigma.com        |
|Zinc Powder      |75      |biggestdrunkard@gmail.com|
|Calcium Carbonate|200     |support@earthworks.au    |
|Phenolphthalein  |5       |contact@sigma.com        |

</details>

So there we can see we have all reagents listed, even if there is no matching supplier (in this case, we have an empty ContactEmail cells)

`RIGHT JOIN` does the same but the opposite. It keeps all data from the right table, and joins data from the left table if there is a matching key:

```
SELECT Reagents.Name, Quantity, ContactEmail
FROM Reagents
RIGHT JOIN Suppliers
  ON Reagents.Manufacturer = Suppliers.Name;
```

<details>
<summary>:star:Output:</summary>
  
|Name             |Quantity|ContactEmail             |
|:---------------:|:------:|:-----------------------:|
|Nitric Acid      |13      |contact@sigma.com        |
|Ethanol          |69      |biggestdrunkard@gmail.com|
|Sulfuric Acid    |2       |contact@sigma.com        |
|Phosphoric Acid  |34      |contact@sigma.com        |
|Uranium          |9001    |biggestdrunkard@gmail.com|
|Hydrochloric Acid|10      |contact@sigma.com        |
|Potassium Iodide |25      |contact@labsource.co.uk  |
|Sodium Hydroxide |100     |contact@sigma.com        |
|Methanol         |500     |biggestdrunkard@gmail.com|
|Ammonium Nitrate |300     |contact@labsource.co.uk  |
|Copper Sulfate   |150     |contact@sigma.com        |
|Zinc Powder      |75      |biggestdrunkard@gmail.com|
|Calcium Carbonate|200     |support@earthworks.au    |
|Phenolphthalein  |5       |contact@sigma.com        |
|                 |        |futuresupplier@gmail.com |

</details>

Since there is no 'Mother Earth' in the right table, we will logically get similar result to the `INNER JOIN` in this case. With an extra added row with the Future Supplier email.
If there were more suppliers in the right table from which we do not have reagents yet, there would also be corresponding rows without Name and Quantity but with ContactEmail data.

## `FULL JOIN` statement

`FULL JOIN` keeps all matching rows from both tables, and all rows with blank data that was unmatched:

```
SELECT Reagents.Name, Quantity, ContactEmail
FROM Reagents
FULL JOIN Suppliers
  ON Reagents.Manufacturer = Suppliers.Name;
```

<details>
<summary>:star:Output:</summary>

|Name             |Quantity|ContactEmail             |
|:---------------:|:------:|:-----------------------:|
|Nitric Acid      |13      |contact@sigma.com        |
|Ethanol          |69      |biggestdrunkard@gmail.com|
|NaCl             |454     |                         |
|Sulfuric Acid    |2       |contact@sigma.com        |
|Phosphoric Acid  |34      |contact@sigma.com        |
|Uranium          |9001    |biggestdrunkard@gmail.com|
|Hydrochloric Acid|10      |contact@sigma.com        |
|Potassium Iodide |25      |contact@labsource.co.uk  |
|Sodium Hydroxide |100     |contact@sigma.com        |
|Methanol         |500     |biggestdrunkard@gmail.com|
|Acetone          |250     |                         |
|Ammonium Nitrate |300     |contact@labsource.co.uk  |
|Copper Sulfate   |150     |contact@sigma.com        |
|Zinc Powder      |75      |biggestdrunkard@gmail.com|
|Calcium Carbonate|200     |support@earthworks.au    |
|Phenolphthalein  |5       |contact@sigma.com        |
|                 |        |futuresupplier@gmail.com |

</details>

## `CROSS JOIN` statement

A little bit more tricky to use in this example. It's a combinatorics!

```
SELECT * FROM Table1
CROSS JOIN Table2;
```

What it would do is create a cartesian product: the result is Table1.rows * Table2.rows.
Since with those two tables there is no logical output at all (and the result is 80 rows), I'll limit the output to 10, in order to show an example:

```
SELECT * FROM Reagents
CROSS JOIN Suppliers
LIMIT 10;
```
<details>
<summary>:star:Output:</summary>
  
|Name       |Concentration|Quantity|Manufacturer |Supplierid|Name-2         |Country  |ContactEmail             |
|:---------:|:-----------:|:------:|:-----------:|:--------:|:-------------:|:-------:|:-----------------------:|
|Nitric Acid|68           |13      |Sigma-Aldrich|2         |Neighbour      |Lithuania|biggestdrunkard@gmail.com|
|Nitric Acid|68           |13      |Sigma-Aldrich|3         |LabSource      |UK       |contact@labsource.co.uk  |
|Nitric Acid|68           |13      |Sigma-Aldrich|4         |EarthWorks     |Australia|support@earthworks.au    |
|Nitric Acid|68           |13      |Sigma-Aldrich|1         |Sigma-Aldrich  |USA      |contact@sigma.com        |
|Nitric Acid|68           |13      |Sigma-Aldrich|5         |Future Supplier|Latvia   |futuresupplier@gmail.com |
|Ethanol    |50           |69      |Neighbour    |2         |Neighbour      |Lithuania|biggestdrunkard@gmail.com|
|Ethanol    |50           |69      |Neighbour    |3         |LabSource      |UK       |contact@labsource.co.uk  |
|Ethanol    |50           |69      |Neighbour    |4         |EarthWorks     |Australia|support@earthworks.au    |
|Ethanol    |50           |69      |Neighbour    |1         |Sigma-Aldrich  |USA      |contact@sigma.com        |
|Ethanol    |50           |69      |Neighbour    |5         |Future Supplier|Latvia   |futuresupplier@gmail.com |

</details>

## Summary with differences

|Join type   |Keeps unmatched left|Keeps unmatched right|Drops unmatched   |Use case                              |
|:----------:|:------------------:|:-------------------:|:----------------:|:------------------------------------:|
|`INNER JOIN`|:x:                 |:x:                  |:white_check_mark:| Only matched rows                    |
|`LEFT JOIN` |:white_check_mark:  |:x:                  | Right only       | All left and matched right           |
|`RIGHT JOIN`|:x:                 |:white_check_mark:   | Left only        | All right and matched left           |
|`FULL JOIN` |:white_check_mark:  |:white_check_mark:   |:x:               | Keep all rows, matched or not        |
|`CROSS JOIN`|:x:                 |:x:                  |:x:               | Combinations (no `ON` condition used)|
