# Word Count using Apache Spark

## Objective

To implement **Word Count using Apache Spark** to count the number of occurrences of each word in a text file.

---

# 1. Start Hadoop Services

Start Hadoop Distributed File System and YARN.

```bash
start-dfs.sh
start-yarn.sh
jps
```

### Verify Running Services

You should see:

```
NameNode
DataNode
ResourceManager
NodeManager
```

---

# 2. Create Input Dataset

Create a text file.

```bash
nano word.txt
```

### Example Dataset

```
this is a demo
this ia a hadoop file
hadoop is big
```

---

# 3. Upload File to HDFS

Create directory in HDFS.

```bash
hadoop fs -mkdir /spark_input
```

Upload dataset.

```bash
hadoop fs -put word.txt /spark_input
```

Verify upload.

```bash
hadoop fs -ls /spark_input
```

Expected output:

```
/spark_input/word.txt
```

---

# 4. Start Spark Shell

```bash
pyspark
```

Spark prompt appears:

```
>>>
```

---

# 5. Load Data from HDFS

```python
lines = sc.textFile("hdfs:///spark_input/word.txt")
```

### Output (lines.collect())

```
['this is a demo',
 'this ia a hadoop file',
 'hadoop is big']
```

---

# 6. Split Lines into Words

```python
words = lines.flatMap(lambda line: line.split(" "))
```

### Output (words.collect())

```
['this',
 'is',
 'a',
 'demo',
 'this',
 'ia',
 'a',
 'hadoop',
 'file',
 'hadoop',
 'is',
 'big']
```

---

# 7. Create Word Pairs

```python
pairs = words.map(lambda word: (word, 1))
```

### Output (pairs.collect())

```
[('this',1),
 ('is',1),
 ('a',1),
 ('demo',1),
 ('this',1),
 ('ia',1),
 ('a',1),
 ('hadoop',1),
 ('file',1),
 ('hadoop',1),
 ('is',1),
 ('big',1)]
```

---

# 8. Count Words

```python
counts = pairs.reduceByKey(lambda a, b: a + b)
```

### Output (counts.collect())

```
[('this',2),
 ('is',2),
 ('a',2),
 ('demo',1),
 ('ia',1),
 ('hadoop',2),
 ('file',1),
 ('big',1)]
```

---

# 9. Display Output

```python
counts.collect()
```

### Final Output

```
[('this',2),
 ('is',2),
 ('a',2),
 ('demo',1),
 ('ia',1),
 ('hadoop',2),
 ('file',1),
 ('big',1)]
```

---

# Spark Processing Flow

```
Input File
     ↓
Load Data (RDD)
     ↓
flatMap → Split Words
     ↓
map → Create (word,1)
     ↓
reduceByKey → Count Words
     ↓
Display Output
```

---

# Result

The Apache Spark program successfully counts the **frequency of each word** in the input dataset using **RDD transformations and actions**.
