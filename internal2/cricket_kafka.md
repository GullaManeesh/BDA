# 🧪 Experiment: Cricket Runs Streaming using Kafka + Spark

## 🎯 Aim
To stream live cricket runs using Kafka and compute total runs in real-time using Spark Structured Streaming.

## 📘 Description
In this experiment, a Kafka producer continuously sends random runs data.  
Spark Structured Streaming consumes this data, converts it into a DataFrame, and calculates total runs dynamically.

## ⚙️ Technologies Used
- Apache Kafka – Used to stream real-time data (runs)
- Apache Spark – Used to process streaming data
- PySpark – Used to write streaming logic in Python

## 🖥️ Commands to Execute

### Terminal 1
bin/zookeeper-server-start.sh config/zookeeper.properties  

### Terminal 2
bin/kafka-server-start.sh config/server.properties  

### Terminal 3 (Producer)
python3 producer.py  

### Terminal 4 (Spark Consumer)
spark-submit consumer.py  

---

## 💻 Full Code
```python
### Producer (producer.py)
from kafka import KafkaProducer  
import json, random, time  

producer = KafkaProducer(  
    bootstrap_servers='localhost:9092',  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  
)  

players = ['Virat', 'Rohit', 'Gill']

while True:
    data = {
        'player': random.choice(players),
        'runs': random.choice([0,1,2,3,4,6])
    }
    print('Sending:', data)
    producer.send('cricket', value=data)
    producer.flush()
    time.sleep(1)

### Spark Consumer (consumer.py)
from pyspark.sql import SparkSession  
from pyspark.sql.functions import *  

spark = SparkSession.builder.appName("Cricket").getOrCreate()  

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","cricket") \
    .load()  

json_df = df.selectExpr("CAST(value AS STRING)")  

runs = json_df.select(
    from_json(col("value"), "player STRING, runs INT").alias("data")
).select("data.*")  

result = runs.agg(sum("runs").alias("total_runs"))  

query = result.writeStream.outputMode("complete").format("console").start()  
query.awaitTermination()  
```
## 📊 Output

Batch 0:  
total_runs = 5  

Batch 1:  
total_runs = 12  

Batch 2:  
total_runs = 20  

---

## ✅ Final Output
The system continuously calculates total runs in real-time:

✔ Data sent by Kafka  
✔ Spark reads and processes it  
✔ Total runs updated continuously  

Example:
Total Runs → 35 → 42 → 50 → ...

---

## 🧠 Key Point
Kafka sends data → Spark converts it into DataFrame → aggregation is done in real-time
