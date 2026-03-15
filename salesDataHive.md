# Sales Data Analysis using Apache Hive

## Objective

To analyze **sales data using Apache Hive** and compute:

* **Total Sales**
* **Region-wise Sales**

---

# 1. Start Hadoop Services

Start Hadoop Distributed File System and YARN.

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

Create a sales dataset.

```bash
nano sales.txt
```

### Example Dataset

```
1 North 5000
2 South 7000
3 East 6000
4 West 8000
5 North 4000
6 South 3000
7 East 2000
```

### Dataset Format

```
SalesID Region SalesAmount
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
CREATE DATABASE salesdb;
```

Check databases:

```sql
SHOW DATABASES;
```

Use the database:

```sql
USE salesdb;
```

---

# 5. Create Hive Table

```sql
CREATE TABLE sales (
id INT,
region STRING,
amount INT
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
sales
```

---

# 6. Load Data into Hive Table

```sql
LOAD DATA LOCAL INPATH 'sales.txt'
INTO TABLE sales;
```

---

# 7. Display Table Data

```sql
SELECT * FROM sales;
```

### Output

```
1 North 5000
2 South 7000
3 East 6000
4 West 8000
5 North 4000
6 South 3000
7 East 2000
```

---

# 8. Total Sales Calculation

Calculate total sales.

```sql
SELECT SUM(amount) AS Total_Sales
FROM sales;
```

### Output

```
35000
```

---

# 9. Region-wise Sales Analysis

```sql
SELECT region, SUM(amount) AS Region_Sales
FROM sales
GROUP BY region;
```

### Output

```
East 8000
North 9000
South 10000
West 8000
```

---

# Hive Processing Flow

```
Create Dataset
       ↓
Create Hive Table
       ↓
Load Data
       ↓
Query using HiveQL
       ↓
Analyze Sales Data
```

---

# Result

The Hive program successfully analyzes the **sales dataset** and calculates:

* **Total sales amount**
* **Region-wise sales distribution**
