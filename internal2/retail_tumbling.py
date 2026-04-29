# 🧪 Experiment: Retail Data using Tumbling Window (Structured Streaming)

## 🎯 Aim
To compute daily revenue per country using a tumbling window on a retail stream with Spark Structured Streaming.

## 📘 Description
This experiment processes streaming retail CSV data and applies a tumbling time window (1 day).  
Each transaction is assigned an event time, and revenue is calculated using TotalPrice.  
The system groups data by country and time window, producing daily revenue per country.  
The output updates as new files are streamed into the system.

## ⚙️ Technologies Used
- Apache Spark – A distributed processing engine that supports real-time analytics using Structured Streaming and window-based computations.

- PySpark – Python interface for Spark used to build streaming applications with DataFrame APIs.

- Structured Streaming – A high-level API that enables processing of streaming data with time-based windows and aggregations.

## 🖥️ Commands to Execute (Step-by-Step)

### Step 1: Install Requirements
sudo apt update  
sudo apt install openjdk-11-jdk -y  
sudo apt install python3-pip -y  

### Step 2: Setup Spark
wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz  
tar -xvzf spark-3.5.1-bin-hadoop3.tgz  
mv spark-3.5.1-bin-hadoop3 ~/spark  

echo 'export SPARK_HOME=~/spark' >> ~/.bashrc  
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc  
source ~/.bashrc  

### Step 3: Create Streaming Folder
mkdir retail_stream  

### Step 4: Stream CSV Files (Terminal 1)
for file in retail_30_days/*.csv; do  
  cp "$file" retail_stream/  
  sleep 2  
done  

### Step 5: Run Program (Terminal 2)
spark-submit tumbling_window.py  

## 💻 Full Code (tumbling_window.py)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, sum, window
from pyspark.sql.types import *

spark = SparkSession.builder.appName('TumblingWindow') \
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
    .csv('retail_stream')

df = df.withColumn('eventTime', to_timestamp(col('InvoiceDate')))
df = df.withColumn('TotalPrice', col('Quantity') * col('UnitPrice'))

result = df.withWatermark('eventTime', '1 day') \
    .groupBy(window(col('eventTime'), '1 day'), col('Country')) \
    .agg(sum('TotalPrice').alias('Revenue'))

query = result.writeStream.outputMode('append') \
    .format('console') \
    .start()

query.awaitTermination()

## 📊 Output at Each Step

### 🔹 Batch 0
(No output initially until data arrives)

### 🔹 Batch 2 (Example)
window                     | Country | Revenue  
2010-12-01                | Italy   | 27734.18  
2010-12-01                | UK      | 27215.65  
2010-12-01                | Spain   | 25059.60  
2010-12-01                | Germany | 27831.26  
2010-11-30                | Spain   | 5673.48  

(As shown in your lab output) :contentReference[oaicite:0]{index=0}  

---

### 🔹 Batch 3
window                     | Country | Revenue  
2010-12-02                | France  | 23688.53  
2010-12-02                | Germany | 27187.26  

---

### 🔹 Later Batches
Each batch shows revenue per country for each 1-day window as new files arrive.

---

## ✅ Final Output
The system continuously outputs daily revenue per country using tumbling windows:

Italy → 27734.18  
UK → 27215.65  
Spain → 25059.60  
Germany → 27831.26  
France → 23688.53  

(Output keeps updating as new CSV files are streamed every 2 seconds)
