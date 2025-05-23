# Altering the table

`ALTER TABLE` statement is used to work with the table / columns (add, rename, remove, change).

## Adding new columns

You can update your table with a new column using the `ADD` statement:

```
ALTER TABLE Reagents
ADD price MONEY; -- MONEY is a data type, a "float" with 2 decimals.
-- 'DEFAULT default_value' could be added to insert a default value if not specified.
```

## Removing data

Be careful when removing data! Before that, check with `SELECT` to be sure you're deleting the right data.

### Dropping a table

DELETES WHOLE TABLE WITH ALL COLUMNS AND DATA!

```
DROP TABLE Reagents;
```

### Dropping a column

You can remove columns with the `DROP` statement.

```
ALTER TABLE Reagents
DROP price;
```

### Dropping a constraint

```
ALTER TABLE Reagents
DROP CONSTRAINT min_price
```

## Renaming

To rename, you can use `RENAME` statement.

### Renaming a table

```
ALTER TABLE Reagents
RENAME TO Supply;
```

### Renaming a column

```
ALTER TABLE Reagents
RENAME price TO cost_price
```

### Renaming a constraint

```
ALTER TABLE Reagents
RENAME CONSTRAINT min_price TO positive_price;
```
