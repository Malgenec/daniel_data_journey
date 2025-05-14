# Cheat Sheet
Basic statements and simple examples will be contained here to help getting used to the syntax.

Here, my goal is to write the statements, explain them and give the examples that I've created. 

_(as a bonus point - I'm learning formatting in GitHub)_
***
## Data Query Language
### SELECT

The main statement which I (and everyone else using SQL) will be going to use.

**SELECT** is used to... select data (lol). _**For example**_:

If we have _**table**_ called _**Reagents**_ as our dataset, which has _**columns**_: _**Name, Concentration, Quantity, Manufacturer**_:

**Reagents**

|Name               |Concentration      |Quantity      |Manufacturer       |
|:-----------------:|:-----------------:|:------------:|:----------------:|
|Nitric Acid        |68                 |13            |Sigma-Aldrich    |
|Ethanol            |50                 |69            |Neighbour         |
|NaCl               |100                |454           |Mother Earth      |
|Sulfuric Acid      |32                 |2             |Sigma-Aldrich    |
|Phosphoric Acid    |40                 |34            |Sigma-Aldrich    |
|Uranium            |100                |9001          |Neighbour         |
|Hydrochloric Acid  |37                 |10            |Sigma-Aldrich    |
|Potassium Iodide   |5                  |25            |LabSource         |
|Sodium Hydroxide   |50                 |100           |Sigma-Aldrich    |
|Methanol           |99                 |500           |Neighbour         |
|Acetone            |100                |250           |Mother Earth      |
|Ammonium Nitrate   |60                 |300           |LabSource         |
|Copper Sulfate     |20                 |150           |Sigma-Aldrich    |
|Zinc Powder        |95                 |75            |Neighbour         |
|Calcium Carbonate  |80                 |200           |EarthWorks        |
|Phenolphthalein    |1                  |5             |Sigma-Aldrich    |

and we want to show all the rows and columns, then, we use asterisk(\*) like this:

```
SELECT * FROM Reagents;
```
Then, we can also select some specific columns to show. For example name and concentration:

```
SELECT Name, Concentration FROM Reagents;
```

Which would show as the following table:

|Name           |Concentration      |
|:-------------:|:-----------------:|
|Nitric Acid    |68                 |
|Ethanol        |50                 |
|NaCl           |100                |
|Sulfuric Acid  |32                 |
|Phosphoric Acid|40                 |
|Uranium        |100                |
|...            |...                |

***
