# 🧪 Experiment: Word Count using Structured Streaming (Apache Spark)

## 🎯 Aim
To perform real-time word count using Apache Spark Structured Streaming.

## 📘 Description
This experiment reads streaming text data from a socket source and processes it in real-time.  
The input text is split into words, grouped, and counted dynamically as new data arrives. The results are continuously displayed on the console using Structured Streaming.

## ⚙️ Technologies Used
- Apache Spark – A unified analytics engine that supports real-time data processing using Structured Streaming with high scalability and fault tolerance.

- Scala – A JVM-based programming language used to write Spark applications efficiently with functional programming features.

- Spark SQL / Structured Streaming – A high-level API in Spark that processes streaming data using DataFrame and SQL operations, enabling real-time analytics.

## 🖥️ Commands to Execute (Ubuntu)

# Start Spark Shell
spark-shell  

## 💻 Full Code
import org.apache.spark.sql.functions._

val df = spark.readStream
  .format("socket")
  .option("host","localhost")
  .option("port",9999)
  .load()

val words = df.selectExpr("explode(split(value,' ')) as word")

val counts = words.groupBy("word").count()

val query = counts.writeStream
  .outputMode("complete")
  .format("console")
  .start()

query.awaitTermination()

## 📊 Output at Each Step
Input Stream (Terminal 1):
hello spark  
hello world  

Streaming Processing:
Data is read line by line from socket  
Words are split into individual tokens  
Word counts are updated continuously  

## ✅ Final Output (Console)
-------------------------------------------
Batch: 0
-------------------------------------------
+-----+-----+
|word |count|
+-----+-----+
|hello|2    |
|spark|1    |
|world|1    |
+-----+-----+

(Output updates continuously as new data is entered)
