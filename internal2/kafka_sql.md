# 🧪 Experiment: Real-Time Stream Processing using Kafka and Flink SQL

## 🎯 Aim
To process real-time streaming data using Apache Kafka and Apache Flink SQL by computing aggregated values over time windows.

## 📘 Description
In this experiment, a Kafka producer continuously sends streaming data with timestamps.  
Apache Flink reads this data as a stream, assigns event-time processing, and applies a tumbling window to compute the sum of values.  
The system processes data in real time and outputs results for every fixed time interval.

## 📌 What is Flink SQL?
Flink SQL is a streaming query engine that allows processing real-time data using SQL queries.  
It supports event-time processing, watermarks, and window-based aggregations.

## ⚙️ Technologies Used
- Apache Kafka – A distributed messaging system used to stream real-time data.

- Apache Flink – A real-time stream processing framework that supports event-time and stateful computations.

- Flink SQL – SQL-based interface for processing streaming data with window functions.

- Python (Kafka Producer) – Used to generate and send streaming data to Kafka.

## 🖥️ Commands to Execute (Step-by-Step)

### Terminal 1: Start ZooKeeper
bin/zookeeper-server-start.sh config/zookeeper.properties  

### Terminal 2: Start Kafka Broker
bin/kafka-server-start.sh config/server.properties  

### Terminal 3: Create Topic
bin/kafka-topics.sh --create --topic flink-stream \
--bootstrap-server localhost:9092 --partitions 1 --replication-factor 1  

### Terminal 4: Start Flink SQL Client
./bin/sql-client.sh embedded  

### Terminal 5: Run Producer
python3 producer.py  

---

## 💻 Full Code

### Kafka Producer (producer.py)
from kafka import KafkaProducer  
import json, time, random  

producer = KafkaProducer(  
    bootstrap_servers='localhost:9092',  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  
)  

while True:  
    data = {  
        "event_time": int(time.time()*1000),  
        "val": random.randint(1,100)  
    }  
    producer.send("flink-stream", value=data)  
    time.sleep(1)  

---

### Flink SQL Table
CREATE TABLE kafka_stream (  
  event_time BIGINT,  
  val INT,  
  rowtime AS TO_TIMESTAMP_LTZ(event_time,3),  
  WATERMARK FOR rowtime AS rowtime - INTERVAL '5' SECOND  
) WITH (  
  'connector'='kafka',  
  'topic'='flink-stream',  
  'properties.bootstrap.servers'='localhost:9092',  
  'format'='json'  
);  

---

### Flink SQL Query
SELECT  
  TUMBLE_START(rowtime, INTERVAL '10' SECOND),  
  SUM(val)  
FROM kafka_stream  
GROUP BY TUMBLE(rowtime, INTERVAL '10' SECOND);  

---

## 📊 Output at Each Step

### 🔹 Producer Output
{"event_time": 1714380000000, "val": 45}  
{"event_time": 1714380001000, "val": 12}  
{"event_time": 1714380002000, "val": 78}  

---

### 🔹 Flink SQL Output
Window Start Time        | Sum(val)  
10:00:00                 | 135  
10:00:10                 | 210  
10:00:20                 | 180  

---

## 📌 Key Concepts

### 🔸 Event Time
Processing is based on actual event timestamp, not system time.

### 🔸 Watermark
Handles late data by allowing delay of 5 seconds.

### 🔸 Tumbling Window
Fixed-size window (10 seconds) with no overlap.

---

## ✅ Final Output
✔ Data is streamed via Kafka  
✔ Flink processes data in real-time  
✔ Aggregation is done using tumbling windows  

Example:
Window 1 → Sum = 135  
Window 2 → Sum = 210  
Window 3 → Sum = 180  

✔ Output updates continuously for every 10-second window
