# 🧪 Experiment: News Clustering using PySpark (K-Means)

## 🎯 Aim
To cluster news articles into different groups using PySpark ML and K-Means clustering.

---

## 📖 Description
This experiment demonstrates **unsupervised learning** using Apache Spark.

News articles are processed using Natural Language Processing (NLP) techniques and grouped into clusters based on similarity.  
Text data is converted into numerical features using TF-IDF, and **K-Means algorithm** is used to cluster similar news articles.

---

## 🛠️ Technologies Used

- **Apache Spark (PySpark)**
  Distributed data processing framework

- **Spark MLlib**
  Machine learning library

- **Python**
  Programming language used

---

## ⚙️ ML & NLP Concepts Used

- **Tokenizer**
  Splits text into words

- **StopWordsRemover**
  Removes common words (like "the", "is")

- **HashingTF**
  Converts text into numerical vectors (term frequency)

- **IDF (Inverse Document Frequency)**
  Assigns importance to words

- **K-Means Clustering**
  Groups similar data into clusters

- **Pipeline**
  Combines all steps into one workflow

---

## 📂 Dataset (news.csv)

```text
text
India wins cricket world cup
New AI technology released by Google
Stock markets rise after budget
Football world championship begins
New smartphone launched by Apple
Government announces new economic policy
Basketball finals attract huge audience
Scientists discover new quantum processor
Startup funding increases in India
Olympics preparation begins
```

---

## 📂 Program Code

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline
import time

spark = SparkSession.builder \
    .appName("NewsClustering") \
    .getOrCreate()

data = spark.read.csv("news.csv", header=True, inferSchema=True)

tokenizer = Tokenizer(inputCol="text", outputCol="words")

remover = StopWordsRemover(inputCol="words", outputCol="filtered")

hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=100)

idf = IDF(inputCol="rawFeatures", outputCol="features")

kmeans = KMeans(k=3, seed=1)

pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, idf, kmeans])

model = pipeline.fit(data)

predictions = model.transform(data)

predictions.select("text","prediction").show(truncate=False)

print("Keeping Spark UI active for 3 minutes to inspect DAG...")
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
news_clustering.py
```

---

## ⚙️ Execution Behavior

- Text data is loaded into DataFrame  
- Tokenizer splits sentences into words  
- Stop words are removed  
- HashingTF converts words into numerical vectors  
- IDF assigns importance to words  
- K-Means groups similar news into clusters  
- Each news article is assigned a cluster ID  

---

## 📊 Output (Sample)

```
+-----------------------------------------------+----------+
|text                                           |prediction|
+-----------------------------------------------+----------+
|India wins cricket world cup                   |0         |
|Football world championship begins             |0         |
|Basketball finals attract huge audience        |0         |
|New AI technology released by Google           |1         |
|Scientists discover new quantum processor      |1         |
|New smartphone launched by Apple               |1         |
|Stock markets rise after budget                |2         |
|Government announces new economic policy       |2         |
|Startup funding increases in India             |2         |
+-----------------------------------------------+----------+
```

---

## ✅ Result

The news articles were successfully clustered into groups using K-Means, and similar articles were grouped together.

---

## 📌 Conclusion

The experiment demonstrated how text data can be processed using NLP techniques and clustered using K-Means in Apache Spark to identify similar news topics.
