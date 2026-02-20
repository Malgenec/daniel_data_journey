# How to use the code:

### Test the import (1k lines)
```python data_to_sql.py 2020_master.txt --test 1000```

### Full import
```python data_to_sql.py 2020_master.txt```

### Check MySQL
```mysql -u root -p nibrs -e "SELECT COUNT(*) FROM incident"```
