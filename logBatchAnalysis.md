# 🧪 Experiment: Log Batch Analysis using PySpark

## 🎯 Aim
To analyze server logs using PySpark and identify the most frequent error messages.

---

## 📖 Description
This experiment demonstrates batch processing of log data using Apache Spark.

The server log file is processed to:
- Filter only error messages  
- Count occurrences of each error  
- Identify the most frequent errors  

RDD transformations are used to process large log data efficiently.

---

## 🛠️ Technologies Used

- **Apache Spark**
  Distributed data processing framework

- **PySpark**
  Python API for Spark

- **Python**
  Used for implementing logic

---

## 📂 Input File (server_log.txt)

Sample log data:

```text
INFO User logged in
ERROR Database connection failed
INFO Request processed
ERROR Timeout occurred
ERROR Database connection failed
WARNING Disk space low
ERROR Timeout occurred
```

---

## 📂 Program Code

```python
from pyspark import SparkContext

sc = SparkContext(appName="LogAnalysisExample")

logs = sc.textFile("file:///home/hduser/spark-26/log_batch_analysis/server_log.txt")

errors = logs.filter(lambda x: "ERROR" in x)

error_counts = errors.map(lambda x: (x,1)).reduceByKey(lambda a,b:a+b)

top_errors = error_counts.take(10)

print("\nMost Frequent Errors:\n")

for error,count in top_errors:
    print(error,count)

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
spark-submit log_analysis.py
```

---

## ⚙️ Execution Behavior

- Log file is read into RDD  
- Only lines containing "ERROR" are filtered  
- Each error is mapped to (error, 1)  
- reduceByKey counts frequency of each error  
- Top errors are retrieved using take(10)  

---

## 📊 Output (Sample)

```
Most Frequent Errors:

ERROR Database connection failed 2
ERROR Timeout occurred 2
```

---

## ✅ Result

The log file was successfully analyzed, and the most frequent error messages were identified using PySpark.

---

## 📌 Conclusion

The experiment demonstrated how batch log analysis can be performed efficiently using Spark RDD transformations to extract meaningful insights from large log data.
