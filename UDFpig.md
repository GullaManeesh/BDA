# User Defined Function (UDF) Implementation in Apache Pig

## Objective

To implement a **Python User Defined Function (UDF) in Apache Pig** to check whether the **temperature quality code is valid** in a weather dataset.

---

# 1. Aim

To implement a **Python UDF in Apache Pig using Jython** to check temperature quality codes in a weather dataset and determine whether the temperature value is valid.

---

# 2. Start Hadoop Services

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

# 3. Sample Weather Dataset

Create dataset file.

```bash
nano weather_data.txt
```

### Example Dataset

```
1901 14 1
1901 -10 1
1901 -19 0
1901 9999 9
1901 0028 1
1901 0030 2
1901 0025 7
1901 0610 3
```

### Dataset Format

```
Year  Temperature  QualityCode
```

---

# 4. Python UDF Program

Create a Python UDF file.

```bash
nano is_good_quality.py
```

### Python UDF Code

```python
@outputSchema("is_good:boolean")
def is_good_quality(q):
    if q is None:
        return False
    valid_codes = ['0','1','4','5','9']
    
   return q in valid_codes
```

### Explanation

The Python UDF:

1. Receives **quality code**
2. Checks if it belongs to valid codes
3. Returns **True if valid**, **False if invalid**

Valid quality codes:

```
0,1,4,5,9
```

---

# 5. Upload Dataset to HDFS

Create HDFS directory.

```bash
hadoop fs -mkdir /weather_udf
```

Upload file.

```bash
hadoop fs -put weather_data.txt /weather_udf
```

Verify upload.

```bash
hadoop fs -ls /weather_udf
```

---

# 6. Start Apache Pig

```bash
pig
```

Pig prompt appears:

```
grunt>
```

---

# 7. Register Python UDF

```pig
REGISTER 'is_good_quality.py' USING jython AS myudfs;
```

---

# 8. Load Weather Dataset

```pig
A = LOAD '/weather_udf/weather_data.txt'
USING PigStorage(' ')
AS (year:int, temp:int, quality:int);
```

---

# 9. Apply UDF Function

```pig
B = FOREACH A GENERATE year, temp, myudfs.is_good_quality(quality);
```

This applies the Python UDF to check the validity of quality code.

---

# 10. Display Result

```pig
DUMP B;
```

### Output Example

```
(1901,14,True)
(1901,-10,True)
(1901,-19,True)
(1901,9999,True)
(1901,28,False)
(1901,30,False)
(1901,25,False)
(1901,610,False)
```

Here:

```
True → Valid quality code
False → Invalid quality code
```

---

# Pig Execution Flow

```
Weather Dataset
      ↓
Load Data
      ↓
Apply Python UDF
      ↓
Validate Quality Code
      ↓
Display Output
```

---

# Result

The **Python User Defined Function (UDF)** is successfully implemented in **Apache Pig** to check whether the **temperature quality code is valid** in the weather dataset.
