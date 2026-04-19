# 🧪 Experiment: Word Count using PySpark (Local Mode)

## 🎯 Aim
To implement a Word Count program using PySpark and execute it in local mode on a single system.

---

## 📖 Description
This experiment demonstrates data processing using Apache Spark in **local mode**.

In this setup, Spark runs entirely on a single machine without any cluster.  
All computations are performed using available CPU cores of the system.

The Word Count program reads a text file, processes the data using RDD transformations, and counts the frequency of each word.

---

## 🛠️ Technologies Used

- **Apache Spark**
  Distributed data processing framework (used here in local mode)

- **PySpark**
  Python API for Apache Spark

- **Python**
  Used to implement the Word Count logic

---

## ⚙️ Execution Mode

- Mode: `local[*]`  
- Meaning: Uses all available CPU cores of the system  
- No Master/Worker nodes required  

---

## 📂 Input File

```text
spark is fast
spark is powerful
big data processing with spark
spark makes distributed computing easy
```

---

## 📂 Program Code

```python
import time
from pyspark import SparkContext

sc = SparkContext(appName="WordCountExample")

text = sc.textFile("input.txt")

counts = (text
          .flatMap(lambda line: line.split(" "))
          .map(lambda word: (word, 1))
          .reduceByKey(lambda a, b: a + b))

for word, count in counts.collect():
    print(word, count)

time.sleep(180)
sc.stop()
```

---

## ▶️ Steps to Execute

### 1. Navigate to Project Folder
```bash
cd ~/spark_local
```

---

### 2. Run PySpark Program
```bash
/usr/local/spark3/bin/spark-submit \
--master local[*] \
--conf spark.pyspark.python=/usr/bin/python3 \
wordcount.py
```

---

## ⚙️ Execution Behavior

- Spark runs locally using all CPU cores  
- No distributed nodes involved  
- Tasks are executed in parallel within the same system  

---

## 📊 Output (Sample)

```
spark 4
is 2
fast 1
powerful 1
big 1
data 1
processing 1
with 1
makes 1
distributed 1
computing 1
easy 1
```

---

## ✅ Result

The Word Count program was successfully executed using PySpark in local mode, and the frequency of each word was obtained.

---

## 📌 Conclusion

The experiment demonstrated how Apache Spark can process data efficiently in local mode using parallel computation without requiring a cluster.
