# 🧪 Experiment: Word Count using Spark Cluster (Distributed Mode)

## 🎯 Aim
To implement a Word Count program using PySpark and execute it on a Spark Cluster (Master–Worker architecture).

---

## 📖 Description
This experiment demonstrates distributed data processing using Apache Spark.  
A Spark cluster consisting of a Master node and Worker node is used to execute a Word Count program.

The Master node handles scheduling and resource allocation, while the Worker node executes tasks in parallel.  
The input data is distributed across the cluster, and the computation is performed using RDD transformations.

---

## 🛠️ Technologies Used

- **Apache Spark (3.5.1)**  
  Distributed data processing framework used to execute tasks in parallel.

- **PySpark**  
  Python API for Apache Spark used to write distributed programs.

- **Ubuntu (20.04 & 22.04)**  
  Operating system used for both Master and Worker nodes.

- **SSH (Secure Shell)**  
  Used for communication between Master and Worker nodes with passwordless login.

- **Python**  
  Programming language used to implement the Word Count logic.

---

## 🌐 Environment Setup

### Master Node
- Hostname: admin38-Vostro-3020-SFF  
- IP Address: 172.16.4.183  
- OS: Ubuntu 20.04  

### Worker Node
- IP Address: 172.16.5.185  
- OS: Ubuntu 22.04  

---

## ⚙️ Spark Cluster Architecture

- Master: 172.16.4.183  
- Worker: 172.16.5.185  

Master → Schedules tasks  
Worker → Executes tasks  

---

## 🐍 Python Configuration Fix

There was a Python version mismatch:

- Master Python: Python 3.8  
- Worker Python: Python 3.10  

### Solution:
- Driver Python: /home/hduser/.pyenv/shims/python3  
- Worker Python: /usr/bin/python3  

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

text = sc.textFile("file:///home/hduser/spark-26/spark_wordcount/input.txt")

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

## ▶️ Steps to Execute (Cluster Mode)

### 1. Start Worker Node
```bash
/usr/local/spark/sbin/start-worker.sh spark://172.16.4.183:7077
```

---

### 2. Transfer Input File to Worker
```bash
scp input.txt hduser@172.16.5.185:/home/hduser/spark-26/spark_wordcount/
```

---

### 3. Run WordCount Program on Cluster
```bash
PYSPARK_DRIVER_PYTHON=/usr/bin/python3 \
PYSPARK_PYTHON=/usr/bin/python3 \
/usr/local/spark/bin/spark-submit \
--master spark://172.16.4.183:7077 \
wordcount.py
```

---

### 4. Run Another Program (Example)
```bash
PYSPARK_DRIVER_PYTHON=/usr/bin/python3 \
PYSPARK_PYTHON=/usr/bin/python3 \
/usr/local/spark/bin/spark-submit \
--master spark://172.16.4.183:7077 \
server_log.py
```

---

## ⚙️ Execution Behavior

- Spark divides the job into multiple tasks  
- Tasks are distributed to worker nodes  
- Execution happens in parallel  

Example log:
```
Starting task ... (172.16.5.185, executor 0)
Finished task ... on 172.16.5.185
```

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

Access cluster monitoring:
```
http://172.16.4.183:8080
```

Displays:
- Worker nodes  
- CPU cores  
- Memory usage  
- Running applications  
- Task execution details  

---

## ✅ Result

The Word Count program was successfully executed on a Spark cluster.  
Distributed processing was achieved by executing tasks across the worker node.

---

## 📌 Conclusion

The Spark cluster was successfully configured and used to execute distributed tasks across multiple machines, demonstrating parallel processing and efficient big data computation.
