## Window Functions
Window functions allow us to create an aggregated column without collapsing rows that we uses for aggregation.

### Syntax:

```
AGG(aggregation_column) OVER(PARTITION BY partition_column)
```
Where AGG - any aggregation function, partition_column - column like the one we would group by.

### Example:

Let's consider we have the following Reagents table:

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

And here we want to add a column, which shows how many types of reagents we have manufactured by the same manufacturer. For that case, we would use:

```
SELECT *,
COUNT(*) OVER(PARTITION BY Manufacturer) AS 'Amount of types per manufacturer'
FROM REAGENTS
```

The resulting output we get:

|Name             |Concentration|Quantity|Volume|Manufacturer |Amount of types per manufacturer|
|:---------------:|:-----------:|:------:|:----:|:-----------:|:------------------------------:|
|Nitric Acid      |68           |13      |1     |Sigma-Aldrich|7                               |
|Ethanol          |50           |69      |5     |Neighbour    |4                               |
|NaCl             |100          |454     |null  |Mother Earth |2                               |
|Sulfuric Acid    |32           |2       |1     |Sigma-Aldrich|7                               |
|Phosphoric Acid  |40           |34      |1     |Sigma-Aldrich|7                               |
|Uranium          |100          |9001    |null  |Neighbour    |4                               |
|Hydrochloric Acid|37           |10      |2     |Sigma-Aldrich|7                               |
|Potassium Iodide |5            |25      |null  |LabSource    |2                               |
|Sodium Hydroxide |50           |100     |null  |Sigma-Aldrich|7                               |
|Methanol         |99           |500     |1     |Neighbour    |4                               |
|Acetone          |100          |250     |5     |Mother Earth |2                               |
|Ammonium Nitrate |60           |300     |1     |LabSource    |2                               |
|Copper Sulfate   |20           |150     |1     |Sigma-Aldrich|7                               |
|Zinc Powder      |95           |75      |null  |Neighbour    |4                               |
|Calcium Carbonate|80           |200     |null  |EarthWorks   |1                               |
|Phenolphthalein  |1            |5       |1     |Sigma-Aldrich|7                               |

If we want to include several columns in partition, we can do it using comma:

```
AGG(aggregation_column) OVER(PARTITION BY partition_column1, partition_column2)
```

### ```OVER()``` with ```ORDER BY```, running sum example

Now let's look at another example, we have a new 'supply' table and we want to calculate a running sum by date.

|product_id|quantity|price|date     |
|:--------:|:------:|:---:|:-------:|
|1         |3       |5.99 |2/16/2026|
|2         |5       |2.99 |2/17/2026|
|3         |6       |7.99 |2/18/2026|
|1         |7       |5.99 |2/19/2026|
|2         |10      |2.99 |2/20/2026|
|3         |15      |7.99 |2/21/2026|
|4         |20      |9.99 |2/22/2026|
|4         |15      |9.99 |2/23/2026|
|2         |10      |2.99 |2/24/2026|

We are able to achieve that using OVER() with ORDER BY:

```
SELECT *,
SUM(price) OVER(ORDER BY date)
FROM supply
```

Output:

|product_id|quantity|price|date     |sum  |
|:--------:|:------:|:---:|:-------:|:---:|
|1         |3       |5.99 |2/16/2026|5.99 |
|2         |5       |2.99 |2/17/2026|8.98 |
|3         |6       |7.99 |2/18/2026|16.97|
|1         |7       |5.99 |2/19/2026|22.96|
|2         |10      |2.99 |2/20/2026|25.95|
|3         |15      |7.99 |2/21/2026|33.94|
|4         |20      |9.99 |2/22/2026|43.93|
|4         |15      |9.99 |2/23/2026|53.92|
|2         |10      |2.99 |2/24/2026|56.91|

Combining OVER(), ORDER BY and PARTITION BY gives a more interesting and practically useful result:

```
SELECT *,
SUM(price) OVER(PARTITION BY product_id ORDER BY date)
FROM supply
```

|product_id|quantity|price|date     |sum  |
|:--------:|:------:|:---:|:-------:|:---:|
|1         |3       |5.99 |2/16/2026|5.99 |
|1         |7       |5.99 |2/19/2026|11.98|
|2         |5       |2.99 |2/17/2026|2.99 |
|2         |10      |2.99 |2/20/2026|5.98 |
|2         |10      |2.99 |2/24/2026|8.97 |
|3         |6       |7.99 |2/18/2026|7.99 |
|3         |15      |7.99 |2/21/2026|15.98|
|4         |20      |9.99 |2/22/2026|9.99 |
|4         |15      |9.99 |2/23/2026|19.98|

That's how we achieve a running sum by product_id, not the whole dataset.

### Identical ORDER BY values

However, if there would be identical date values, there would be no addition of the second identical date value. By default, order by contains the following: ```RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW```

If there was a need to calculate it row by row, we should have done it by adding ```ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW```, like there:

```
SELECT *,
SUM(price) OVER(ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
FROM supply
```
