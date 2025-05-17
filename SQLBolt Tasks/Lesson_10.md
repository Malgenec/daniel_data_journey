## Table: Employees

|Role    |Name      |Building|Years_employed|
|:------:|:--------:|:------:|:------------:|
|Engineer|Becky A.  |1e      |4             |
|Engineer|Dan B.    |1e      |2             |
|Engineer|Sharon F. |1e      |6             |
|Engineer|Dan M.    |1e      |4             |
|Engineer|Malcom S. |1e      |1             |
|Artist  |Tylar S.  |2w      |2             |
|Artist  |Sherman D.|2w      |8             |
|Artist  |Jakob J.  |2w      |6             |
|Artist  |Lillia A. |2w      |7             |
|Artist  |Brandon J.|2w      |7             |
|Manager |Scott K.  |1e      |9             |
|Manager |Shirlee M.|1e      |3             |
|Manager |Daria O.  |2w      |6             |

### Task 1

Find the longest time that an employee has been at the studio

```
SELECT MAX(Years_employed) AS Max_Years_Employed
FROM Employees;
```

### Task 2

For each role, find the average number of years employed by employees in that role

```
SELECT Role, AVG(Years_employed) AS Average_Years_Employed
FROM Employees
GROUP BY Role;
```

### Task 3

Find the total number of employee years worked in each building

```
SELECT Building, SUM(Years_employed) AS Total_Years_Employed
FROM Employees
GROUP BY Building;
```
