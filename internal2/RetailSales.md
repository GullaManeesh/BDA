# 🧪 Experiment 4: Retail Stream (Cumulative Revenue)

## 🎯 Aim
To compute running cumulative revenue per country from a retail CSV stream using Spark Structured Streaming.

## 📘 Description
This experiment processes streaming retail data from CSV files.  
Each incoming file contains transaction details, and Spark continuously reads new files as a stream.  
A new column (TotalPrice) is calculated, and cumulative revenue is computed per country.  
The output updates dynamically as new files are added to the stream directory.

## ⚙️ Technologies Used
- Apache Spark – A distributed processing engine that supports real-time data processing using Structured Streaming with high scalability and fault tolerance.

- PySpark – Python API for Spark that enables easy development of streaming and batch applications using DataFrame operations.

- Structured Streaming – A Spark API that processes streaming data as continuous tables and allows real-time aggregation and analysis.

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

### Step 3: Prepare Streaming Folder
mkdir retail_stream  

### Step 4: Start Streaming (Terminal 1 – simulate files)
while true; do  
  cp sample.csv retail_stream/  
  sleep 2  
done  

### Step 5: Run Program (Terminal 2)
spark-submit retail_stream.py  

## 💻 Full Code (retail_stream.py)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, sum
from pyspark.sql.types import *

spark = SparkSession.builder.appName('Retail30DaysStreaming') \
    .config('spark.hadoop.fs.defaultFS', 'file:///').getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

schema = StructType([
    StructField("InvoiceNo", StringType()),
    StructField("StockCode", StringType()),
    StructField("Description", StringType()),
    StructField("Quantity", IntegerType()),
    StructField("InvoiceDate", StringType()),
    StructField("UnitPrice", DoubleType()),
    StructField("CustomerID", StringType()),
    StructField("Country", StringType())
])

df = spark.readStream.option('header', True).schema(schema) \
    .csv('retail_stream/')

df = df.withColumn('InvoiceTimestamp', to_timestamp(col('InvoiceDate')))
df = df.withColumn('TotalPrice', col('Quantity') * col('UnitPrice'))

result = df.groupBy('Country').agg(sum('TotalPrice').alias('Revenue'))

query = result.writeStream.outputMode('complete') \
    .format('console') \
    .start()

query.awaitTermination()

## 📊 Output at Each Step

### 🔹 Batch 0 (Initial)
Country      | Revenue  
Germany      | 20472.34  
France       | 23448.28  
Italy        | 23371.58  
Spain        | 22236.63  
UK           | 21253.53  
Netherlands  | 22429.13  

### 🔹 Intermediate Batches
As more CSV files are added every 2 seconds, revenue increases continuously.

Example (as seen in your lab output) :contentReference[oaicite:0]{index=0}:

Batch 1:
Germany | 68178.14  
France  | 71363.98  
Italy   | 70932.59  
Spain   | 69236.97  
UK      | 66939.88  
Netherlands | 68769.10  

Batch 2:
Germany | 98838.16  
France  | 93038.36  
Italy   | 96229.83  
Spain   | 91115.98  
UK      | 88950.49  
Netherlands | 92113.45  

---

### 🔹 Final Batch (Example)
Batch 27:
Germany    | 701183.85  
France     | 689881.49  
Italy      | 691842.37  
Spain      | 670980.70  
UK         | 683036.08  
Netherlands| 675844.66  

---

## ✅ Final Output
The system continuously updates cumulative revenue per country as new data streams in:

Germany → 701183.85  
France → 689881.49  
Italy → 691842.37  
Spain → 670980.70  
UK → 683036.08  
Netherlands → 675844.66  

(Output keeps updating as new CSV files are streamed every 2 seconds)
