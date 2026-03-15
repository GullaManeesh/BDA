# Create Tables and Load Data in Apache Hive (All Basic Commands)

## Objective

To create a **table in Apache Hive**, load data, and perform **INSERT, SELECT, UPDATE, DELETE, and ALTER operations** on the Hive table.

---

# 1. Start Hadoop Services

Start Hadoop Distributed File System and YARN.

```bash
start-dfs.sh
start-yarn.sh
jps
```

### Verify Running Services

```
NameNode
DataNode
ResourceManager
NodeManager
```

---

# 2. Create Input Dataset

```bash
nano employee.txt
```

### Example Dataset

```
1 John 50000
2 Alice 60000
3 Bob 45000
4 David 70000
```

### Dataset Format

```
ID Name Salary
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

# 4. Create Database

```sql
CREATE DATABASE company;
```

Show databases:

```sql
SHOW DATABASES;
```

Output example:

```
default
company
```

Use the database:

```sql
USE company;
```

---

# 5. Create Hive Table

```sql
CREATE TABLE employee (
id INT,
name STRING,
salary INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ' ';
```

Check tables:

```sql
SHOW TABLES;
```

Output:

```
employee
```

---

# 6. Load Data into Table

```sql
LOAD DATA LOCAL INPATH 'employee.txt'
INTO TABLE employee;
```

---

# 7. Display Table Data

```sql
SELECT * FROM employee;
```

Output

```
1 John 50000
2 Alice 60000
3 Bob 45000
4 David 70000
```

---

# 8. Insert Data into Table

```sql
INSERT INTO employee VALUES (5,'Maneesh',65000);
```

Check data:

```sql
SELECT * FROM employee;
```

Output

```
1 John 50000
2 Alice 60000
3 Bob 45000
4 David 70000
5 Maneesh 65000
```

---

# 9. Conditional Query

```sql
SELECT name, salary
FROM employee
WHERE salary > 50000;
```

Output

```
Alice 60000
David 70000
Maneesh 65000
```

---

# 10. UPDATE Command

Hive supports update when **ACID tables** are enabled.

Example:

```sql
UPDATE employee
SET salary = 75000
WHERE name='David';
```

Check result:

```sql
SELECT * FROM employee;
```

Output

```
1 John 50000
2 Alice 60000
3 Bob 45000
4 David 75000
5 Maneesh 65000
```

---

# 11. DELETE Command

```sql
DELETE FROM employee
WHERE name='Bob';
```

Check result:

```sql
SELECT * FROM employee;
```

Output

```
1 John 50000
2 Alice 60000
4 David 75000
5 Maneesh 65000
```

---

# 12. ALTER TABLE Commands

## 12.1 Rename Table

```sql
ALTER TABLE employee RENAME TO staff;
```

Check tables:

```sql
SHOW TABLES;
```

Output

```
staff
```

---

## 12.2 Add Column

```sql
ALTER TABLE staff ADD COLUMNS (department STRING);
```

Describe table:

```sql
DESCRIBE staff;
```

Output

```
id INT
name STRING
salary INT
department STRING
```

---

## 12.3 Change Column Name

```sql
ALTER TABLE staff CHANGE salary emp_salary INT;
```

Describe table:

```sql
DESCRIBE staff;
```

Output

```
id INT
name STRING
emp_salary INT
department STRING
```

---

## 12.4 Replace Columns

```sql
ALTER TABLE staff REPLACE COLUMNS (
id INT,
name STRING,
salary INT
);
```

Output

```
Columns replaced successfully
```

---

## 12.5 Rename Column

```sql
ALTER TABLE staff CHANGE name employee_name STRING;
```

Output

```
id INT
employee_name STRING
salary INT
```

---

# 13. Drop Table

```sql
DROP TABLE staff;
```

Check tables:

```sql
SHOW TABLES;
```

Output

```
No tables found
```

---

# Hive Processing Flow

```
Create Dataset
       ↓
Create Database
       ↓
Create Table
       ↓
Load Data
       ↓
Insert / Update / Delete
       ↓
Alter Table
       ↓
Query Data
```

---

# Result

The Hive database and table were successfully created. Data was loaded and various HiveQL operations such as **INSERT, SELECT, UPDATE, DELETE, and ALTER TABLE** were executed successfully.

