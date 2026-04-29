# 🧪 Experiment: Cricket Score Analytics using Kafka + Spark Structured Streaming

## 🎯 Aim
To stream live cricket score data through Kafka and process it using Spark Structured Streaming to compute player statistics and strike rate in real time.

## 📘 Description
This experiment demonstrates real-time data processing using Kafka and Spark.  
A Kafka producer continuously sends cricket data (player and runs).  
Spark Structured Streaming consumes this data, aggregates total runs and balls per player, and calculates strike rate dynamically.  
The results update continuously as new data streams in.

## 📌 What is Strike Rate?
Strike Rate = (Total Runs / Balls Faced) × 100  
It measures how quickly a player scores runs in cricket.

## ⚙️ Technologies Used
- Apache Kafka – A distributed streaming platform used to send and receive real-time data using producer-consumer architecture.

- Apache Spark Structured Streaming – Processes real-time data streams and performs aggregation and analytics.

- PySpark – Python API for Spark used to build streaming analytics applications.

## 🖥️ Commands to Execute (Step-by-Step)

### Terminal 1: Start ZooKeeper
bin/zookeeper-server-start.sh config/zookeeper.properties  

### Terminal 2: Start Kafka Broker
bin/kafka-server-start.sh config/server.properties  

### Terminal 3: Create Topic
bin/kafka-topics.sh --create --topic cricket \
--bootstrap-server 127.0.0.1:9092 --partitions 1 --replication-factor 1  

### Terminal 4: Run Spark Consumer
spark-submit --master local[*] \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 \
cricket_spark.py  

### Terminal 5: Run Producer
python3 cricket_producer.py  

(As shown in your lab execution) :contentReference[oaicite:0]{index=0}  

## 💻 Full Code

```
### Producer (cricket_producer.py)
from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:9092',
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

### Spark Consumer (cricket_spark.py)
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, sum as _sum, count
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder.appName('CricketAnalytics') \
    .master('local[*]').getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

schema = StructType() \
    .add('player', StringType()) \
    .add('runs', IntegerType())

df = spark.readStream.format('kafka') \
    .option('kafka.bootstrap.servers', '127.0.0.1:9092') \
    .option('subscribe', 'cricket') \
    .option('startingOffsets', 'latest') \
    .load()

json_df = df.selectExpr('CAST(value AS STRING)')

parsed = json_df.select(from_json(col('value'), schema).alias('data'))

player_df = parsed.select('data.player', 'data.runs')

stats = player_df.groupBy('player').agg(
    _sum('runs').alias('total_runs'),
    count('runs').alias('balls')
)

stats = stats.withColumn(
    'strike_rate',
    (col('total_runs')/col('balls'))*100
)

query = stats.writeStream.outputMode('complete') \
    .format('console') \
    .start()

query.awaitTermination()

```

## 📊 Output at Each Step

### 🔹 Producer Output
Sending: {'player': 'Virat', 'runs': 4}  
Sending: {'player': 'Rohit', 'runs': 1}  
Sending: {'player': 'Gill', 'runs': 6}  

---

### 🔹 Streaming Output (Spark)

Batch 63:
player | total_runs | balls | strike_rate  
Rohit  | 53         | 21    | 252.38  
Virat  | 40         | 19    | 210.52  
Gill   | 70         | 24    | 291.66  

Batch 65:
player | total_runs | balls | strike_rate  
Rohit  | 55         | 23    | 239.13  
Virat  | 40         | 19    | 210.52  
Gill   | 70         | 24    | 291.66  

---

## ✅ Final Output
The system continuously computes real-time cricket statistics:

✔ Total runs per player  
✔ Balls faced per player  
✔ Strike rate calculation  

Example:
Rohit → 55 runs, SR = 239.13  
Virat → 40 runs, SR = 210.52  
Gill → 70 runs, SR = 291.66  

✔ Output updates dynamically as new data arrives from Kafka  
✔ Demonstrates real-time analytics using Kafka + Spark
