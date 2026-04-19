# 🧪 Experiment: Word Count using PySpark

## 🎯 Aim

To implement a Word Count program using PySpark and execute it on an Ubuntu system.

---

## 📖 Description

Word Count is a basic data processing program used to count the frequency of words in a text file.  
In this experiment, PySpark is used to:

- Read a text file
- Split lines into words
- Map each word to a key-value pair (word, 1)
- Reduce by key to count occurrences

---

## 🛠️ Requirements

- Ubuntu OS
- Apache Spark installed
- Python installed
- Java installed

---

## 📂 Program Code

```python
from pyspark import SparkContext

sc = SparkContext(appName="WordCountExample")

# Read text file
text = sc.textFile("file:///home/hduser/spark-26/spark_wordcount/input.txt")

# Word count logic
counts = (text
          .flatMap(lambda line: line.split(" "))
          .map(lambda word: (word, 1))
          .reduceByKey(lambda a, b: a + b))

# Print result
for word, count in counts.collect():
    print(word, count)

sc.stop()
```

---

## ▶️ Steps to Execute (Ubuntu)

### 1. Open Terminal

```
Ctrl + Alt + T
```

### 2. Navigate to Spark Directory

```bash
cd /home/hduser/spark-26/
```

### 3. Create Project Folder (if not created)

```bash
mkdir spark_wordcount
cd spark_wordcount
```

### 4. Create Input File

```bash
nano input.txt
```

Add sample text:

```
hello world hello spark
```

Save and exit:

- Ctrl + X
- Y
- Enter

---

### 5. Create Python File

```bash
nano wordcount.py
```

Paste your PySpark code and save:

- Ctrl + X
- Y
- Enter

---

### 6. Set Environment Variables (if required)

```bash
export SPARK_HOME=/home/hduser/spark-26
export PATH=$PATH:$SPARK_HOME/bin
```

---

### 7. Run PySpark Program

```bash
spark-submit wordcount.py
```

---

## 📊 Output

```
hello 2
world 1
spark 1
```

---

## ✅ Result

The Word Count program was successfully executed using PySpark, and the frequency of each word in the input file was obtained.
