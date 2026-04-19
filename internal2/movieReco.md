# 🧪 Experiment: Movie Recommendation System using PySpark (ALS)

## 🎯 Aim
To build a movie recommendation system using PySpark MLlib and predict user preferences using the ALS algorithm.

---

## 📖 Description
This experiment demonstrates a **collaborative filtering recommendation system** using Apache Spark.

The dataset contains user ratings for movies.  
The **ALS (Alternating Least Squares)** algorithm is used to learn patterns from user–movie interactions and recommend movies.

The model predicts ratings and suggests top movies for each user.

---

## 🛠️ Technologies Used

- **Apache Spark (PySpark)**
  Distributed data processing framework

- **Spark MLlib**
  Machine learning library used for recommendation

- **Python**
  Programming language used for implementation

---

## ⚙️ ML Concepts Used

- **ALS (Alternating Least Squares)**
  Collaborative filtering algorithm for recommendations

- **RegressionEvaluator**
  Used to evaluate model performance (RMSE)

---

## 📂 Dataset

Dataset used: MovieLens dataset  
:contentReference[oaicite:0]{index=0}

### Ratings File Structure (ratings.csv)
```text
userId,movieId,rating,timestamp
```

---

## 📂 Program Code

```python
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder \
    .appName("MovieRecommendation") \
    .getOrCreate()

# Load ratings data
ratings = spark.read.csv("ratings.csv", header=True, inferSchema=True)
ratings = ratings.select("userId","movieId","rating")

# Split data
(training, test) = ratings.randomSplit([0.8,0.2])

# ALS model
als = ALS(
    userCol="userId",
    itemCol="movieId",
    ratingCol="rating",
    coldStartStrategy="drop",
    nonnegative=True
)

model = als.fit(training)

# Predictions
predictions = model.transform(test)

# Evaluate model
evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="rating",
    predictionCol="prediction"
)

rmse = evaluator.evaluate(predictions)

print("Root Mean Square Error =", rmse)

# Recommend movies for users
userRecs = model.recommendForAllUsers(5)

userRecs.show(5, False)

import time
time.sleep(120)

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
movie_recommendation.py
```

---

## ⚙️ Execution Behavior

- Dataset is loaded into DataFrame  
- Data is split into training and testing sets  
- ALS model learns user–movie interaction patterns  
- Predictions are generated for test data  
- Model accuracy is evaluated using RMSE  
- Top 5 movie recommendations are generated for each user  

---

## 📊 Output (Sample)

```
Root Mean Square Error = 0.89

+------+------------------------------------------+
|userId|recommendations                           |
+------+------------------------------------------+
|1     |[{50, 4.5}, {172, 4.3}, ...]              |
|2     |[{10, 4.7}, {200, 4.4}, ...]              |
+------+------------------------------------------+
```

---

## ✅ Result

The movie recommendation system was successfully implemented using the ALS algorithm, and personalized movie recommendations were generated for users.

---

## 📌 Conclusion

The experiment demonstrated how collaborative filtering using ALS can be applied in Apache Spark to build scalable recommendation systems based on user preferences.
