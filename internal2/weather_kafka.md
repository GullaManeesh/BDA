# 🧪 Experiment: Weather Alert System using Kafka (Producer & Consumer)

## 🎯 Aim
To build a real-time weather alert system using Kafka where a producer streams city temperatures and a consumer raises alerts for high temperatures.

## 📘 Description
This experiment uses Apache Kafka for real-time data streaming.  
A producer continuously sends temperature data for multiple cities to a Kafka topic.  
A consumer reads this data in real time and triggers alerts if temperature exceeds a threshold (≥ 40°C).  
This demonstrates real-time event processing using a publish-subscribe model.

## 📌 What is Kafka?
Apache Kafka is a distributed streaming platform used for real-time data pipelines.  
It follows a **publish-subscribe model** where:
- Producers send data to topics
- Consumers read data from topics  

It is widely used for real-time analytics and streaming applications.

## ⚙️ Technologies Used
- Apache Kafka – A distributed messaging system used for real-time data streaming and event-driven processing.

- Python (Kafka-Python) – Used to implement producer and consumer applications that send and receive streaming data.

- ZooKeeper – Used by Kafka to manage cluster coordination and broker metadata.

## 🖥️ Commands to Execute (Step-by-Step)

### Terminal 1: Start ZooKeeper
bin/zookeeper-server-start.sh config/zookeeper.properties  

### Terminal 2: Start Kafka Broker
bin/kafka-server-start.sh config/server.properties  

### Terminal 3: Run Producer
python3 weather_producer.py  

### Terminal 4: Run Consumer
python3 weather_consumer.py  


## 💻 Full Code

### Producer (weather_producer.py)

```python
from kafka import KafkaProducer
import json, random, time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

cities = ['New York', 'London', 'Mumbai', 'Tokyo', 'Sydney']

def generate_temperature():
    return random.randint(20, 45)

while True:
    for city in cities:
        data = {'city': city, 'temperature': generate_temperature()}
        print(f'Sending: {data}')
        producer.send('weather_updates', value=data)
        time.sleep(1)

### Consumer (weather_consumer.py)
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'weather_updates',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='weather-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Listening for weather updates...")

for message in consumer:
    data = message.value
    city = data['city']
    temp = data['temperature']

    if temp >= 40:
        print(f'ALERT: {city} temperature is {temp}°C')
    else:
        print(f'{city}: ok')
```

## 📊 Output at Each Step

### 🔹 Producer Output
Sending: {'city': 'New York', 'temperature': 39}  
Sending: {'city': 'London', 'temperature': 35}  
Sending: {'city': 'Mumbai', 'temperature': 24}  
Sending: {'city': 'Tokyo', 'temperature': 34}  
Sending: {'city': 'Sydney', 'temperature': 31}  

---

### 🔹 Consumer Output
Listening for weather updates...

New York: ok  
London: ok  
Mumbai: ok  
Tokyo: ok  
Sydney: ok  

ALERT: New York temperature is 42°C  
ALERT: Mumbai temperature is 41°C  
ALERT: Tokyo temperature is 40°C  
ALERT: London temperature is 44°C  
ALERT: Sydney temperature is 45°C  

---

## ✅ Final Output
The system continuously processes real-time temperature data and generates alerts:

✔ If temperature ≥ 40°C → ALERT  
✔ If temperature < 40°C → ok  

Example:
ALERT: Mumbai temperature is 45°C  
London: ok  
Tokyo: ok  

The consumer successfully receives live data from Kafka and triggers alerts in real time.
