## Creating a table

To create a table, we can use `CREATE` statement:

```
CREATE TABLE IF NOT EXISTS table1 (
    column1 DataType TableConstraint DEFAULT default_value,
    column2 DataType TableConstraint DEFAULT default_value,
    ...
);
```

Here, `IF NOT EXISTS` helps to avoid the error and not create the table if there is a table with the same name.

`DEFAULT` lets specify default value if no value is written.

Data types and Table constraint can be found below:

## Data types

There are many data types in different SQL databases. 
Since I use PostgreSQL I'll leave the table from the PostgreSQL documentation

<details>
<summary>PostgreSQL Types of data </summary>
*

Table was copied from this [source](https://www.postgresql.org/docs/current/datatype.html)
  
|Name                                   |Aliases           |Description                                                     |
|:-------------------------------------:|:----------------:|:--------------------------------------------------------------:|
|bigint                                 |int8              |signed eight-byte integer                                       |
|bigserial                              |serial8           |autoincrementing eight-byte integer                             |
|bit [ (n) ]                            |                  |fixed-length bit string                                         |
|bit varying [ (n) ]                    |varbit [ (n) ]    |variable-length bit string                                      |
|boolean                                |bool              |logical Boolean (true/false)                                    |
|box                                    |                  |rectangular box on a plane                                      |
|bytea                                  |                  |binary data ( byte array )                                      |
|character [ (n) ]                      |char [ (n) ]      |fixed-length character string                                   |
|character varying [ (n) ]              |varchar [ (n) ]   |variable-length character string                                |
|cidr                                   |                  |IPv4 or IPv6 network address                                    |
|circle                                 |                  |circle on a plane                                               |
|date                                   |                  |calendar date (year, month, day)                                |
|double precision                       |float8            |double precision floating-point number (8 bytes)                |
|inet                                   |                  |IPv4 or IPv6 host address                                       |
|integer                                |int, int4         |signed four-byte integer                                        |
|interval [ fields ] [ (p) ]            |                  |time span                                                       |
|json                                   |                  |textual JSON data                                               |
|jsonb                                  |                  |binary JSON data, decomposed                                    |
|line                                   |                  |infinite line on a plane                                        |
|lseg                                   |                  |line segment on a plane                                         |
|macaddr                                |                  |MAC (Media Access Control) address                              |
|macaddr8                               |                  |MAC (Media Access Control) address (EUI-64 format)              |
|money                                  |                  |currency amount                                                 |
|numeric [ (p, s) ]                     |decimal [ (p, s) ]|exact numeric of selectable precision                           |
|path                                   |                  |geometric path on a plane                                       |
|pg_lsn                                 |                  |PostgreSQL Log Sequence Number                                  |
|pg_snapshot                            |                  |user-level transaction ID snapshot                              |
|point                                  |                  |geometric point on a plane                                      |
|polygon                                |                  |closed geometric path on a plane                                |
|real                                   |float4            |single precision floating-point number (4 bytes)                |
|smallint                               |int2              |signed two-byte integer                                         |
|smallserial                            |serial2           |autoincrementing two-byte integer                               |
|serial                                 |serial4           |autoincrementing four-byte integer                              |
|text                                   |                  |variable-length character string                                |
|time [ (p) ] [ without time zone ]     |                  |time of day (no time zone)                                      |
|time [ (p) ] with time zone            |timetz            |time of day, including time zone                                |
|timestamp [ (p) ] [ without time zone ]|                  |date and time (no time zone)                                    |
|timestamp [ (p) ] with time zone       |timestamptz       |date and time, including time zone                              |
|tsquery                                |                  |text search query                                               |
|tsvector                               |                  |text search document                                            |
|txid_snapshot                          |                  |user-level transaction ID snapshot (deprecated; see pg_snapshot)|
|uuid                                   |                  |universally unique identifier                                   |
|xml                                    |                  |XML data                                                        |
</details>

<details>
<summary>PostgreSQL Numeric types of data </summary>
*

Table was copied from this [source](https://www.postgresql.org/docs/current/datatype-numeric.html)

|Name            |Storage Size|Description                    |Range                                                                                   |
|:--------------:|:----------:|:-----------------------------:|:--------------------------------------------------------------------------------------:|
|smallint        |2 bytes     |small-range integer            |-32768 to +32767                                                                        |
|integer         |4 bytes     |typical choice for integer     |-2147483648 to +2147483647                                                              |
|bigint          |8 bytes     |large-range integer            |-9223372036854775808 to +9223372036854775807                                            |
|decimal         |variable    |user-specified precision, exact|up to 131072 digits before the decimal point; up to 16383 digits after the decimal point|
|numeric         |variable    |user-specified precision, exact|up to 131072 digits before the decimal point; up to 16383 digits after the decimal point|
|real            |4 bytes     |variable-precision, inexact    |6 decimal digits precision                                                              |
|double precision|8 bytes     |variable-precision, inexact    |15 decimal digits precision                                                             |
|smallserial     |2 bytes     |small autoincrementing integer |1 to 32767                                                                              |
|serial          |4 bytes     |autoincrementing integer       |1 to 2147483647                                                                         |
|bigserial       |8 bytes     |large autoincrementing integer |1 to 9223372036854775807                                                                |

To configure the precision and scale of numeric (or decimal too), use:

```
NUMERIC(precision, scale) -- the maximum precision is 1000
precision - maximum number of digits that are present in a number (including decimals places)
scale - maximum number of decimal places
```

</details>

<details>
<summary>PostgreSQL Character types of data </summary>
*

Tables were copied from this [source](https://www.postgresql.org/docs/current/datatype-character.html)

|Name                            |Description                             |
|:------------------------------:|:--------------------------------------:|
|character varying(n), varchar(n)|variable-length with limit              |
|character(n), char(n), bpchar(n)|fixed-length, blank-padded              |
|bpchar                          |variable unlimited length, blank-trimmed|
|text                            |variable unlimited length               |

Special types:

|Name  |Storage Size|Description                   |
|:----:|:----------:|:----------------------------:|
|"char"|1 byte      |single-byte internal type     |
|name  |64 bytes    |internal type for object names|

</details>

<details>
<summary>PostgreSQL Date/Time types of data </summary>
*

Table was copied from this [source](https://www.postgresql.org/docs/current/datatype-datetime.html)
    
|Name                                   |Storage Size|Description                          |Low Value       |High Value     |Resolution   |
|:-------------------------------------:|:----------:|:-----------------------------------:|:--------------:|:-------------:|:-----------:|
|timestamp [ (p) ] [ without time zone ]|8 bytes     |both date and time (no time zone)    |4713 BC         |294276 AD      |1 microsecond|
|timestamp [ (p) ] with time zone       |8 bytes     |both date and time, with time zone   |4713 BC         |294276 AD      |1 microsecond|
|date                                   |4 bytes     |date (no time of day)                |4713 BC         |5874897 AD     |1 day        |
|time [ (p) ] [ without time zone ]     |8 bytes     |time of day (no date)                |00:00:00        |24:00:00       |1 microsecond|
|time [ (p) ] with time zone            |12 bytes    |time of day (no date), with time zone|00:00:00+1559   |24:00:00-1559  |1 microsecond|
|interval [ fields ] [ (p) ]            |16 bytes    |time interval                        |-178000000 years|178000000 years|1 microsecond|

</details>

## Data constraints

Several data constraints exist in SQL, which give more control over data in a column provided. If data violates a constraint, error is being raised.

### `CHECK` constraint

`CHECK` constraint allows to specify a boolean rule, for example:

```
CREATE TABLE REAGENTS (
name varchar(255),
concentration INTEGER CHECK (concentration <= 100 AND concentration > 0)
);
```

To specify name of a constraint, use `CONSTRAINT`:

```
CREATE TABLE REAGENTS (
name varchar(255),
quantity INTEGER  CONSTRAINT positive_quantity CHECK (quantity >= 0)
);
```

### `NOT NULL` constraint

The following constraint is used to ensure the data is not empty (`NULL`):

```
CREATE TABLE Reagents (
name text NOT NULL
);
```

It's a more efficient equivalent of `CHECK (name IS NOT NULL)`.


### `UNIQUE` constraint

`UNIQUE` constraint makes sure your data won't be repeated (unless data is `NULL`):

```
CREATE TABLE Reagents (
some_id INTEGER UNIQUE
);
```

or if you want to make several columns unique:

```
CREATE TABLE Reagents (
some_id INTEGER
unique_name TEXT
other_value INTEGER
UNIQUE (id, unique_name)
);
```

For non-null unique values:

```
CREATE TABLE Reagents (
some_id INTEGER UNIQUE NULLS NOT DISTINCT
);
```

### `PRIMARY KEY` constraint

`PRIMARY KEY` is a constraint which makes a column values be an unique identifiers (both UNIQUE and NOT NULL)

```
CREATE TABLE Reagents (
unique_id INTEGER PRIMARY KEY
);
```

There can be several primary keys, the syntax is the same as for `UNIQUE` constraint.

### `FOREIGN KEY` and `REFERENCES` constraints

`FOREIGN KEY` is a constraint which makes a `REFERENCE` to match column value to another table's column values.

```
CREATE TABLE Main_table (
name TEXT PRIMARY KEY
);
```

```
CREATE TABLE Other_table (
name TEXT REFERENCES Main_table (name)
);
```

### Additional rules for `REFERENCES` constraint

There are some additional options to be considered for a foreign key. `ON DELETE` specifies what to do with the child row if the parent row is deleted. There are a few follow-ups:

- `RESTRICT` - prevents deletion of a child row
- `CASCADE` - child row gets deleted too
- `NO ACTION` - raise an error (default)
- `SET NULL` - child row changes to `NULL` values
- `SET DEFAULT` - child row changes to default values specified before.

There is also `ON UPDATE` that specifies behaviour of the child row when the parent row is updated. Follow-ups:

- `RESTRICT` prevents update of a child row
- `CASCADE` updates foreign keys in child rows
- `NO ACTION` raises an error

Example:

```
CREATE TABLE Parent_table (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);
```

```
CREATE TABLE Child_table (
    id INTEGER PRIMARY KEY
    name TEXT NOT NULL
    Child_id INTEGER
    FOREIGN KEY (Child_id) REFERENCES Parent_table(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
```

To be continued...
