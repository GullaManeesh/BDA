# Hive User Defined Function (UDF) using Python

## Objective

To implement a **User Defined Function (UDF) in Apache Hive using Python** to perform custom processing on Hive table data.

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

Create a sample dataset.

```bash
nano numbers.txt
```

### Example Dataset

```
1
2
3
4
5
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
CREATE TABLE numbers (
num INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\n';
```

---

# 5. Load Data into Hive Table

```sql
LOAD DATA LOCAL INPATH 'numbers.txt'
INTO TABLE numbers;
```

---

# 6. Create Python UDF Script

Create Python file.

```bash
nano square_udf.py
```

### Python UDF Code

```python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    num = int(line.strip())
    print(num * num)
```

### Explanation

The Python UDF:

1. Reads numbers from standard input
2. Calculates the **square of each number**
3. Prints the result

Example:

```
3 → 9
4 → 16
```

---

# 7. Give Execution Permission

```bash
chmod +x square_udf.py
```

---

# 8. Use Python UDF in Hive

Run query using **TRANSFORM**.

```sql
SELECT TRANSFORM(num)
USING 'python3 square_udf.py'
AS squared_value
FROM numbers;
```

---

# Output

```
1
4
9
16
25
```

---

# Hive Python UDF Processing Flow

```
Hive Table
     ↓
TRANSFORM Clause
     ↓
Python Script Execution
     ↓
Return Processed Data
```

---

# Result

The **Python User Defined Function (UDF)** is successfully implemented in **Hive using the TRANSFORM clause** to compute the **square of numbers** stored in the Hive table.
