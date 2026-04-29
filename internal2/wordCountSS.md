# 🧪 Experiment 3: Word Count (Live Socket Stream)

## 🎯 Aim
To perform live word count from a socket stream using Spark Structured Streaming.

## 📘 Description
This experiment processes real-time streaming data using Apache Spark Structured Streaming.  
Text data is continuously read from a socket (localhost:9999), split into words, grouped, and counted dynamically.  
The output updates continuously as new data arrives, enabling real-time analytics.

## ⚙️ Technologies Used
- Apache Spark – A powerful distributed data processing engine that supports real-time stream processing using Structured Streaming with fault tolerance and scalability.

- PySpark – Python API for Apache Spark that allows writing Spark applications using Python, making it easy to process large-scale streaming data.

- Structured Streaming – A high-level streaming API in Spark that treats streaming data as a continuous table and allows real-time processing using DataFrame operations.

## 🖥️ Commands to Execute (Step-by-Step)


### Step 1: Open Terminal 1 (Start Socket Stream)
nc -lk 9999  

### Step 2: Open Terminal 2 (Run Program)
spark-submit wordcount_stream.py  

## 💻 Full Code (wordcount_stream.py)
```python

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

spark = SparkSession.builder.appName('LiveWordCount') \
    .master('local[*]').getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

df = spark.readStream.format('socket') \
    .option('host', 'localhost') \
    .option('port', 9999).load()

words = df.select(explode(split(df.value, ' ')).alias('word'))

wordCounts = words.groupBy('word').count()

query = wordCounts.writeStream.outputMode('complete') \
    .format('console') \
    .option('truncate', False) \
    .option('checkpointLocation', '/tmp/wordcount_checkpoint') \
    .start()

query.awaitTermination()

```

## 📊 Output at Each Step

### 🔹 Terminal 1 Input (Live Stream)
hi  
hello  
hadoop  
hadoop  
bda  
bda bda  

(As shown in your lab output) :contentReference[oaicite:0]{index=0}

---

### 🔹 Streaming Output (Terminal 2)

Batch 1:
word | count  
hi   | 1  

Batch 2:
word | count  
hello | 1  
hi    | 1  

Batch 3:
word | count  
hello  | 1  
hi     | 1  
hadoop | 1  

Batch 4:
word | count  
hello  | 1  
hi     | 1  
hadoop | 2  

Batch 5:
word | count  
hello  | 1  
bda    | 1  
hi     | 1  
hadoop | 2  

Batch 6:
word | count  
hello  | 1  
bda    | 3  
hi     | 1  
hadoop | 2  

---

## ✅ Final Output
The output continuously updates showing cumulative word counts in real-time:

hello → 1  
hi → 1  
hadoop → 2  
bda → 3  

(Output keeps updating as new words are entered)
