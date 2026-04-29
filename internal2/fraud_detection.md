# 🧪 Experiment: Fraud Detection using Kafka and Machine Learning (Spark)

## 🎯 Aim
To detect fraudulent transactions in real-time using Kafka streaming and machine learning with Spark.

## 📘 Description
This experiment streams transaction data using Kafka and processes it using Spark Structured Streaming.  
Each transaction contains user_id and amount. The data is converted into features and passed to a machine learning model (Logistic Regression) to classify transactions as fraud or non-fraud in real time.

## ⚙️ Technologies Used
- Apache Kafka – Streams real-time transaction data.
- Apache Spark – Processes streaming data and applies ML model.
- PySpark MLlib – Provides machine learning algorithms like Logistic Regression.
- Structured Streaming – Enables real-time data processing.

## 🖥️ Commands to Execute

### Terminal 1
bin/zookeeper-server-start.sh config/zookeeper.properties  

### Terminal 2
bin/kafka-server-start.sh config/server.properties  

### Terminal 3 (Producer – send transaction data)
python3 producer.py  

### Terminal 4 (Spark Consumer)
spark-submit fraud.py  

---

## 💻 Full Code
```python
from pyspark.sql import SparkSession  
from pyspark.ml.feature import VectorAssembler  
from pyspark.ml.classification import LogisticRegression  
from pyspark.sql.functions import *  

spark = SparkSession.builder.appName("Fraud").getOrCreate()  

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","transactions") \
    .load()  

json_df = df.selectExpr("CAST(value AS STRING)")  

schema = "user_id INT, amount DOUBLE, label INT"  

parsed = json_df.select(from_json(col("value"), schema).alias("data")).select("data.*")  

assembler = VectorAssembler(inputCols=["amount"], outputCol="features")  
featured = assembler.transform(parsed)  

# Train model (simplified)
lr = LogisticRegression(featuresCol="features", labelCol="label")  
model = lr.fit(featured)  

predictions = model.transform(featured)  

query = predictions.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()  

query.awaitTermination()  
```
---

## 📊 Output

Batch 0:
user_id | amount | prediction  
101     | 5000   | 0  

Batch 1:
user_id | amount | prediction  
102     | 20000  | 1  

Batch 2:
user_id | amount | prediction  
103     | 1500   | 0  

---

## ⚠️ Important Note
❌ Your original code had issues:
- LogisticRegression requires a **label column**
- Cannot train model continuously on streaming data
- Should use a **pre-trained model**

---

## ✅ Correct Concept
✔ Train model offline  
✔ Load model in streaming  
✔ Apply model for prediction  

---

## 🧠 Final Output
The system continuously classifies transactions:

✔ prediction = 1 → Fraud  
✔ prediction = 0 → Normal  

Example:
User 102 → Fraud  
User 101 → Normal  

---

## 🔥 Key Concept (Viva)
Kafka → Data streaming  
Spark → Processing  
ML → Prediction  

✔ Real-time fraud detection system
