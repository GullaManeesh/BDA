# 🧪 Experiment: Retail Data using Sliding Window (Structured Streaming)

## 🎯 Aim
To compute revenue using a sliding window (1-day window, 5-minute slide) on a retail stream with Spark Structured Streaming.

## 📘 Description
This experiment processes streaming retail CSV data and applies a sliding time window.  
Each transaction is assigned an event time, and TotalPrice is calculated.  
Unlike tumbling windows, sliding windows overlap, producing more frequent and detailed revenue updates per country.  
The output updates continuously as new files are streamed.

## 📌 What is Sliding Window?
A sliding window is a time-based window that overlaps with other windows.  
It has:
- Window size (duration of data considered)
- Slide interval (how often the window moves)

Example:
Window size = 1 day, Slide = 5 minutes  
👉 Every 5 minutes, a new window is created covering the last 1 day of data  

This produces overlapping results → more fine-grained analysis.

## ⚙️ Technologies Used
- Apache Spark – A distributed engine for large-scale data processing that supports real-time analytics using Structured Streaming.

- PySpark – Python API for Spark used to develop streaming applications with simple DataFrame operations.

- Structured Streaming – Spark API that enables real-time data processing with support for window-based aggregations.

## 🖥️ Commands to Execute (Step-by-Step)

### Step 1: Stream CSV Files (Terminal 1)
for file in retail_30_days/*.csv; do  
  cp "$file" retail_stream2/  
  sleep 2  
done  

(As shown in your lab setup) :contentReference[oaicite:0]{index=0}  

### Step 2: Run Program (Terminal 2)
spark-submit sliding_window.py  

## 💻 Full Code (sliding_window.py)

```python 
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, sum, window
from pyspark.sql.types import *

spark = SparkSession.builder.appName('SlidingWindow') \
    .config('spark.hadoop.fs.defaultFS', 'file:///').getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

schema = StructType([
    StructField('InvoiceNo', StringType()),
    StructField('StockCode', StringType()),
    StructField('Description', StringType()),
    StructField('Quantity', IntegerType()),
    StructField('InvoiceDate', StringType()),
    StructField('UnitPrice', DoubleType()),
    StructField('CustomerID', StringType()),
    StructField('Country', StringType())
])

df = spark.readStream.option('header', True).schema(schema) \
    .csv('retail_stream2')

df = df.withColumn('eventTime', to_timestamp(col('InvoiceDate')))
df = df.withColumn('TotalPrice', col('Quantity') * col('UnitPrice'))

result = df.withWatermark('eventTime', '1 day') \
    .groupBy(window(col('eventTime'), '1 day', '5 minutes'), col('Country')) \
    .agg(sum('TotalPrice').alias('Revenue'))

query = result.writeStream.outputMode('append') \
    .format('console') \
    .start()

query.awaitTermination()

```

## 📊 Output at Each Step

### 🔹 Batch 2 (Example)
window                        | Country | Revenue  
2010-12-02 19:25 → ...       | Germany | 236.44  
2010-12-02 13:20 → ...       | UK      | 236.52  
2010-12-01 16:30 → ...       | France  | 246.66  
2010-12-01 03:50 → ...       | Italy   | 380.20  

---

### 🔹 Batch 32
window                        | Country | Revenue  
2010-12-27 05:30 → ...       | UK      | 24710.76  
2010-12-27 05:30 → ...       | Germany | 33008.89  

---

### 🔹 Batch 34
window                        | Country | Revenue  
2010-12-28 05:30 → ...       | Spain   | 30225.10  
2010-12-28 05:30 → ...       | Italy   | 32364.33  

---

## ✅ Final Output
Sliding window continuously produces overlapping revenue results:

Germany → 33008.89  
UK → 24710.76  
Spain → 30225.10  
Italy → 32364.33  
France → 246.66  

✔ Provides more detailed and frequent updates compared to tumbling window  
✔ Output updates every 5 minutes for the last 1-day data window  
