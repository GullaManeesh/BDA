# 🧪 Experiment: Fraud Detection using PySpark (Machine Learning)

## 🎯 Aim
To implement a fraud detection system using PySpark ML and classify transactions as fraudulent or non-fraudulent.

---

## 📖 Description
This experiment demonstrates the use of **Machine Learning in Apache Spark** for detecting fraudulent transactions.

The dataset contains transaction details such as amount, location, merchant, and device.  
Categorical data is converted into numerical format using indexing, and a **Random Forest Classifier** is used to predict fraud.

The model is built using a **Pipeline**, which automates preprocessing and model training steps.

---

## 🛠️ Technologies Used

- **Apache Spark (PySpark)**
  Distributed data processing framework

- **Spark MLlib**
  Machine learning library in Spark

- **Python**
  Programming language used for implementation

---

## ⚙️ ML Concepts Used

- **StringIndexer**
  Converts categorical data into numerical indices

- **VectorAssembler**
  Combines multiple columns into a single feature vector

- **Random Forest Classifier**
  Supervised learning algorithm used for classification

- **Pipeline**
  Chains multiple stages into a single workflow

---

## 📂 Dataset (transactions.csv)

```text
amount,location,merchant,device,fraud
120,India,Amazon,Mobile,0
5000,USA,Apple,Laptop,0
50,India,Flipkart,Mobile,0
20000,Nigeria,Unknown,Mobile,1
15000,Nigeria,Unknown,Tablet,1
80,India,Swiggy,Mobile,0
30000,Russia,Unknown,Laptop,1
60,India,Amazon,Mobile,0
25000,Russia,Unknown,Mobile,1
90,India,Zomato,Mobile,0
```

---

## 📂 Program Code

```python
from pyspark.sql import SparkSession
import time
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline

spark = SparkSession.builder \
    .appName("FraudDetection") \
    .getOrCreate()

data = spark.read.csv("transactions.csv", header=True, inferSchema=True)

location_index = StringIndexer(inputCol="location", outputCol="locationIndex")
merchant_index = StringIndexer(inputCol="merchant", outputCol="merchantIndex")
device_index = StringIndexer(inputCol="device", outputCol="deviceIndex")

assembler = VectorAssembler(
    inputCols=["amount","locationIndex","merchantIndex","deviceIndex"],
    outputCol="features"
)

rf = RandomForestClassifier(labelCol="fraud", featuresCol="features")

pipeline = Pipeline(stages=[location_index, merchant_index, device_index, assembler, rf])

model = pipeline.fit(data)

predictions = model.transform(data)

predictions.select("amount","location","fraud","prediction").show()

time.sleep(180)

spark.stop()
```

---

## ▶️ Steps to Execute

### 1. Navigate to Project Folder
```bash
cd ~/spark_local
```

---

### 2. Run PySpark Program
```bash
/usr/local/spark3/bin/spark-submit \
--master local[*] \
fraud_detection.py
```

---

## ⚙️ Execution Behavior

- Dataset is loaded into Spark DataFrame  
- Categorical columns are converted to numeric values  
- Features are combined into a feature vector  
- Random Forest model is trained  
- Predictions are generated for each transaction  

---

## 📊 Output (Sample)

```
+------+--------+-----+----------+
|amount|location|fraud|prediction|
+------+--------+-----+----------+
|   120|   India|    0|       0.0|
|  5000|     USA|    0|       0.0|
| 20000| Nigeria|    1|       1.0|
| 30000|  Russia|    1|       1.0|
+------+--------+-----+----------+
```

---

## ✅ Result

The fraud detection model was successfully implemented using PySpark ML, and transactions were classified as fraudulent or non-fraudulent.

---

## 📌 Conclusion

The experiment demonstrated how machine learning techniques in Apache Spark can be used to detect fraudulent transactions efficiently using distributed data processing.
