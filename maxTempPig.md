# Maximum Temperature Analysis using Apache Pig

## Objective

To analyze a **weather dataset using Apache Pig** and determine the **maximum temperature recorded for each year**.

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

Create a dataset file.

```bash
nano weather.txt
```

### Example Dataset

```
2010 32
2010 35
2011 30
2011 40
2012 28
2012 33
```

### Dataset Format

```
Year Temperature
```

---

# 3. Upload Dataset to HDFS

Create directory in HDFS.

```bash
hadoop fs -mkdir /pig_weather
```

Upload dataset.

```bash
hadoop fs -put weather.txt /pig_weather
```

Verify upload.

```bash
hadoop fs -ls /pig_weather
```

Expected output:

```
/pig_weather/weather.txt
```

---

# 4. Start Apache Pig

Run Pig in MapReduce mode.

```bash
pig
```

Pig prompt appears:

```
grunt>
```

---

# 5. Load Weather Dataset

```pig
A = LOAD '/pig_weather/weather.txt'
USING PigStorage(' ')
AS (year:int, temp:int);
```

### Relation A

```
(2010,32)
(2010,35)
(2011,30)
(2011,40)
(2012,28)
(2012,33)
```

---

# 6. Group Data by Year

```pig
B = GROUP A BY year;
```

### Relation B

```
(2010,{(2010,32),(2010,35)})
(2011,{(2011,30),(2011,40)})
(2012,{(2012,28),(2012,33)})
```

---

# 7. Find Maximum Temperature

```pig
C = FOREACH B GENERATE group, MAX(A.temp);
```

### Relation C

```
(2010,35)
(2011,40)
(2012,33)
```

---

# 8. Display Output

```pig
DUMP C;
```

### Final Output

```
(2010,35)
(2011,40)
(2012,33)
```

---

# Pig Execution Flow

```
Weather Dataset
      ↓
Load Data
      ↓
Group by Year
      ↓
Find Maximum Temperature
      ↓
Display Output
```

---

# Result

The Apache Pig program successfully analyzes the weather dataset and determines the **maximum temperature recorded for each year**.
