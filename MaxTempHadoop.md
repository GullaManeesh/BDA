# Weather Dataset Analysis – Maximum Temperature using MapReduce (Hadoop Streaming)

## Objective

To analyze a **weather dataset** and find the **maximum temperature for each year** using **Hadoop MapReduce with Python (Hadoop Streaming)**.

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

# 2. Create Project Files

Create three files:

```
mapper.py
reducer.py
weather.txt
```

---

# 3. Create Input Dataset

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

Each line contains:

```
Year Temperature
```

---

# 4. Mapper Program

Create mapper file.

```bash
nano mapper.py
```

```python
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    year, temp = line.strip().split()
    print(f"{year}\t{temp}")
```

### Mapper Explanation

The mapper:

1. Reads input line by line
2. Splits **year and temperature**
3. Emits key-value pair

```
Year → Key
Temperature → Value
```

### Mapper Output Example

```
2010    32
2010    35
2011    30
2011    40
2012    28
2012    33
```

---

# 5. Reducer Program

Create reducer file.

```bash
nano reducer.py
```

```python
#!/usr/bin/env python3

import sys

current_year = None
max_temp = float('-inf')

for line in sys.stdin:
    year, temp = line.strip().split("\t")
    temp = int(temp)

    if current_year == year:
        max_temp = max(temp, max_temp)

    else:
        if current_year:
            print(f"{current_year},{max_temp}")

        current_year = year
        max_temp = temp

if current_year:
    print(f"{year},{max_temp}")
```

### Reducer Explanation

The reducer:

1. Receives **sorted mapper output**
2. Groups data by **year**
3. Calculates **maximum temperature**
4. Prints result for each year

---

# 6. Test Mapper and Reducer Locally

Before running Hadoop, test locally.

```bash
cat weather.txt | python3 mapper.py | sort -k1,1 | python3 reducer.py
```

### Output

```
2010,35
2011,40
2012,33
```

Explanation:

```
2010 → max(32,35) = 35
2011 → max(30,40) = 40
2012 → max(28,33) = 33
```

---

# 7. Upload Dataset to HDFS

Create HDFS directory.

```bash
hadoop fs -mkdir /weather
```

Upload dataset.

```bash
hadoop fs -put weather.txt /weather
```

Verify upload.

```bash
hadoop fs -ls /weather
```

Expected output:

```
/weather/weather.txt
```

---

# 8. Give Execution Permission

```bash
chmod +x mapper.py
chmod +x reducer.py
```

---

# 9. Run Hadoop Streaming Job

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file mapper.py \
-mapper mapper.py \
-file reducer.py \
-reducer reducer.py \
-input /weather/weather.txt \
-output /weather_output
```

---

# 10. Check Output Directory

```bash
hadoop fs -ls /weather_output
```

You should see:

```
part-00000
_SUCCESS
```

---

# 11. View Final Output

```bash
hadoop fs -cat /weather_output/part-00000
```

### Final Output

```
2010,35
2011,40
2012,33
```

---

# MapReduce Processing Flow

```
Weather Dataset
       ↓
Mapper → (year, temperature)
       ↓
Shuffle & Sort
       ↓
Reducer → Maximum temperature per year
       ↓
Output
```

---

# Result

The Hadoop MapReduce program successfully analyzes the weather dataset and calculates the **maximum temperature for each year**.
