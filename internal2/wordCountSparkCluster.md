# 🧪 Experiment: Word Count using Spark Cluster (Single System - Pseudo Distributed Mode)

## 🎯 Aim
To implement a Word Count program using PySpark and execute it on a Spark cluster simulated on a single system (pseudo-distributed mode).

---

## 📖 Description
This experiment demonstrates distributed data processing using Apache Spark on a single machine by simulating a cluster environment.

Both the Master and Worker nodes run on the same system.  
The Master node handles scheduling and resource allocation, while the Worker node executes tasks in parallel.

This setup is called **pseudo-distributed mode**, where distributed computing concepts are demonstrated without multiple physical machines.

---

## 🛠️ Technologies Used

- **Apache Spark**
  Distributed data processing framework.

- **PySpark**
  Python API for writing Spark applications.

---

## ⚙️ Cluster Architecture (Single System)

- Master: localhost  
- Worker: localhost  

👉 Both run on the same machine

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

## ▶️ Steps to Execute (Single System Cluster)

### 1. Navigate to Spark Directory
```bash
cd /usr/local/spark
```

---

### 2. Start Master Node
```bash
./sbin/start-master.sh
```

👉 Open Web UI:
```
http://localhost:8080
```

👉 Note Master URL (example):
```
spark://localhost:7077
```

---

### 3. Start Worker Node (Same System)
```bash
./sbin/start-worker.sh spark://localhost:7077
```

---

### 4. Go to Project Folder
```bash
cd ~/spark_local
```

---

### 5. Run Word Count Program
```bash
/usr/local/spark/bin/spark-submit \
--master spark://localhost:7077 \
wordcount.py
```

---

## ⚙️ Execution Behavior

- Spark divides the job into multiple tasks  
- Tasks are executed by the worker (same system)  
- Parallel execution is simulated  

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

## 🌐 Spark Web UI

```
http://localhost:8080
```

Displays:
- Worker node  
- CPU usage  
- Memory usage  
- Running jobs  

---

## ✅ Result

The Word Count program was successfully executed using a Spark cluster simulated on a single system, demonstrating distributed processing.

---

## 📌 Conclusion

A pseudo-distributed Spark cluster was created on a single machine by running both master and worker processes locally, successfully demonstrating parallel data processing.
