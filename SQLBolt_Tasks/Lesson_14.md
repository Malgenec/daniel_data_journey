## Table: Movies

|Id |Title              |Director      |Year|Length_minutes|
|:-:|:-----------------:|:------------:|:--:|:------------:|
|1  |Toy Story          |John Lasseter |1995|81            |
|2  |A Bug's Life       |El Directore  |1998|95            |
|3  |Toy Story 2        |John Lasseter |1899|93            |
|4  |Monsters, Inc.     |Pete Docter   |2001|92            |
|5  |Finding Nemo       |Andrew Stanton|2003|107           |
|6  |The Incredibles    |Brad Bird     |2004|116           |
|7  |Cars               |John Lasseter |2006|117           |
|8  |Ratatouille        |Brad Bird     |2007|115           |
|9  |WALL-E             |Andrew Stanton|2008|104           |
|10 |Up                 |Pete Docter   |2009|101           |
|11 |Toy Story 8        |El Directore  |2010|103           |
|12 |Cars 2             |John Lasseter |2011|120           |
|13 |Brave              |Brenda Chapman|2012|102           |
|14 |Monsters University|Dan Scanlon   |2013|110           |

### Task 1

The director for A Bug's Life is incorrect, it was actually directed by John Lasseter

A data-check (to not mess up the table):

```
SELECT * FROM Movies
WHERE Title = "A Bug's Life";
```

Solution:

```
UPDATE Movies
SET Director = 'John Lasseter'
WHERE Title = "A Bug's Life";
```

### Task 2

The year that Toy Story 2 was released is incorrect, it was actually released in 1999

Check:

```
SELECT * FROM Movies
WHERE Title = 'Toy Story 2';
```

Solution:

```
UPDATE Movies
SET Year = 1999
WHERE Title = 'Toy Story 2';
```

### Task 3

Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich

Check:

```
SELECT * FROM Movies
WHERE Title = 'Toy Story 8';
```

Solution:

```
UPDATE Movies
SET Title = 'Toy Story 3',
    Director = 'Lee Unkrich'
WHERE Title = 'Toy Story 8';
```
