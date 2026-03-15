# Hive User Defined Function (UDF) using Python – Maximum Salary in Each Department

## Objective

To implement a **Python UDF in Apache Hive** to calculate the **maximum salary in each department** of a company dataset.

---

# 1. Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
jps
```

### Verify Running Services

You should see:

```
NameNode
DataNode
ResourceManager
NodeManager
```

---

# 2. Create Input Dataset

Create dataset file.

```bash
nano employee.txt
```

### Example Dataset

```
1 HR 50000
2 HR 60000
3 IT 70000
4 IT 65000
5 Sales 55000
6 Sales 75000
```

### Dataset Format

```
ID Department Salary
```

---

# 3. Start Hive

```bash
hive
```

Hive prompt appears:

```
hive>
```

---

# 4. Create Hive Table

```sql
CREATE TABLE employee (
id INT,
dept STRING,
salary INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ' ';
```

---

# 5. Load Data into Hive Table

```sql
LOAD DATA LOCAL INPATH 'employee.txt'
INTO TABLE employee;
```

---

# 6. Verify Table Data

```sql
SELECT * FROM employee;
```

### Output

```
1 HR 50000
2 HR 60000
3 IT 70000
4 IT 65000
5 Sales 55000
6 Sales 75000
```

---

# 7. Create Python UDF Script

Create Python script.

```bash
nano max_salary_udf.py
```

### Python Code

```python
#!/usr/bin/env python3
import sys

current_dept = None
max_salary = 0

for line in sys.stdin:
    dept, salary = line.strip().split()
    salary = int(salary)

    if current_dept == dept:
        max_salary = max(max_salary, salary)
    else:
        if current_dept:
            print(current_dept, max_salary)

        current_dept = dept
        max_salary = salary

if current_dept:
    print(current_dept, max_salary)
```

---

# 8. Give Execution Permission

```bash
chmod +x max_salary_udf.py
```

---

# 9. Apply Python UDF in Hive

```sql
SELECT TRANSFORM(dept, salary)
USING 'python3 max_salary_udf.py'
AS (dept STRING, max_salary INT)
FROM (
SELECT dept, salary FROM employee
SORT BY dept
) t;
```

---

# Output

```
HR 60000
IT 70000
Sales 75000
```

---

# Processing Flow

```
Hive Table
     ↓
Send Data to Python Script
     ↓
Python Calculates Maximum Salary
     ↓
Return Result to Hive
```

---

# Result

The **Python UDF in Hive** successfully calculates the **maximum salary for each department** in the company dataset.
