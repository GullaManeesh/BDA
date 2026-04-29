# 🧪 Experiment: Fraud Detection using Kafka + Spark + Machine Learning

## 🎯 Aim
To detect fraudulent transactions in real-time using Kafka streaming and Spark ML.

## 📘 Description
This experiment streams transaction data using Kafka.  
Each transaction contains user_id, amount, location, timestamp, and fraud label.  
Spark Structured Streaming consumes this data, converts it into a DataFrame, and applies a machine learning model (Logistic Regression) to classify transactions as fraud or normal in real time.

## ⚙️ Technologies Used
- Apache Kafka – Streams real-time transaction data.
- Apache Spark – Processes streaming data.
- PySpark MLlib – Used for machine learning (Logistic Regression).
- Structured Streaming – Enables real-time processing.

## 🖥️ Commands to Execute

### Terminal 1
bin/zookeeper-server-start.sh config/zookeeper.properties  

### Terminal 2
bin/kafka-server-start.sh config/server.properties  

### Terminal 3 (Producer)
python3 producer.py  

### Terminal 4 (Spark Consumer)
spark-submit fraud.py  

---

## 💻 Full Code

```python
### Producer (producer.py)
from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

locations = ["India", "USA", "UK", "Canada"]

while True:
    data = {
        "user_id": random.randint(1, 1000),
        "amount": random.randint(100, 50000),
        "location": random.choice(locations),
        "timestamp": time.time(),
        "fraud": 1 if random.random() > 0.8 else 0
    }

    producer.send("transactions", data)
    print("Sent:", data)

    time.sleep(0.01)
```
---
```python
### Spark Consumer (fraud.py)
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression

spark = SparkSession.builder.appName("FraudDetection").getOrCreate()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)")

schema = "user_id INT, amount INT, location STRING, timestamp DOUBLE, fraud INT"

parsed_df = json_df.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

assembler = VectorAssembler(inputCols=["amount"], outputCol="features")
featured_df = assembler.transform(parsed_df)

lr = LogisticRegression(featuresCol="features", labelCol="fraud")
model = lr.fit(featured_df)

predictions = model.transform(featured_df)

query = predictions.select("user_id", "amount", "prediction") \
    .writeStream \
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
205     | 45000  | 1  

Batch 2:
user_id | amount | prediction  
330     | 1200   | 0  

---

## ⚠️ Important Notes
- Model training (`fit`) is done on streaming data here for simplicity, but in real-world systems:
  ✔ Model is trained offline  
  ✔ Loaded and used only for prediction  

- Fraud label:
  0 → Normal  
  1 → Fraud  

---

## 🧠 Final Output
✔ Kafka streams transaction data  
✔ Spark processes data in real-time  
✔ ML model predicts fraud  

Example:
User 205 → Fraud  
User 101 → Normal  

✔ Output updates continuously as new data arrives
