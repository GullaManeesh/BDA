# 🧪 Experiment: Sentiment Analysis using PySpark (NLP - Logistic Regression)

## 🎯 Aim
To perform sentiment analysis on customer reviews using PySpark and classify them as positive or negative.

---

## 📖 Description
This experiment demonstrates **Natural Language Processing (NLP)** using Apache Spark.

Text data (customer reviews) is processed and converted into numerical features using TF-IDF.  
A **Logistic Regression model** is used to classify sentiments.

The system predicts whether a review is **positive or negative** along with probability.

---

## 🛠️ Technologies Used

- **Apache Spark (PySpark)**  
  Distributed data processing framework  

- **Spark MLlib**  
  Machine learning library  

- **Python**  
  Programming language  

---

## ⚙️ NLP & ML Concepts Used

- **Tokenizer** → Splits text into words  
- **StopWordsRemover** → Removes common words  
- **HashingTF** → Converts words into vectors  
- **IDF** → Assigns importance to words  
- **StringIndexer** → Converts labels to numeric  
- **Logistic Regression** → Classification model  
- **Pipeline** → Combines all steps  

---

## 📂 Dataset (reviews.csv)

```text
text,sentiment
Worst purchase ever,negative
Great experience overall,positive
I love this product,positive
Terrible customer service,negative
...
```

---

## 📂 Program Code

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

spark = SparkSession.builder.appName("SparkSentimentAnalysisDemo").getOrCreate()

data = spark.read.csv(
 "file:///home/hduser/spark-26/spark_nlp_sentiment_demo/reviews.csv",
 header=True, inferSchema=True
)

data = data.repartition(10)

label_indexer = StringIndexer(inputCol="sentiment", outputCol="label")

tokenizer = Tokenizer(inputCol="text", outputCol="words")

remover = StopWordsRemover(inputCol="words", outputCol="filtered")

hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=1000)

idf = IDF(inputCol="rawFeatures", outputCol="features")

lr = LogisticRegression(maxIter=10)

pipeline = Pipeline(stages=[label_indexer, tokenizer, remover, hashingTF, idf, lr])

model = pipeline.fit(data)

predictions = model.transform(data)

predictions.select("text", "prediction", "probability").show(20, truncate=False)

input("Press Enter to stop Spark...")

spark.stop()
```

---

## ▶️ Steps to Execute

### 1. Navigate to Project Folder
```bash
cd ~/spark_local
```

---

### 2. Run Program
```bash
/usr/local/spark3/bin/spark-submit \
--master local[*] \
sentiment_analysis.py
```

---

## ⚙️ Execution Behavior

- Dataset is loaded into DataFrame  
- Data is repartitioned for parallel processing  
- Text is tokenized into words  
- Stop words are removed  
- Words are converted into TF vectors  
- IDF assigns importance to words  
- Logistic Regression learns sentiment patterns  
- Model predicts sentiment and probability  

---

## 📊 Output (Sample)

```
text                     prediction    probability
Worst purchase ever      1.0           [3.25E-7, 0.999999...]
Great experience overall 0.0           [0.9998, 0.0002...]
I love this product      0.0           [0.998, 0.002...]
```

---

## 🔍 Output Meaning

- **prediction**
  - `0.0` → Positive  
  - `1.0` → Negative  

- **probability**
  - Confidence score for each class  

---

## ✅ Result

The sentiment analysis model successfully classified customer reviews into positive and negative categories along with prediction probabilities.

---

## 📌 Conclusion

The experiment demonstrated how NLP techniques combined with Logistic Regression can be used in Apache Spark to perform sentiment classification on large-scale text data efficiently.
