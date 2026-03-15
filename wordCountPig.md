# Word Count using Apache Pig (Hadoop Mode)

## Objective

To perform **Word Count using Apache Pig on Hadoop (MapReduce mode)** and understand how Pig Latin processes data stored in **HDFS**.

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

# 2. Create Input File

Create a sample text file in the local system.

```bash
nano word.txt
```

### Example Content

```
hello hadoop
hello big data
hadoop big data
```

---

# 3. Upload File to HDFS

Create a directory in HDFS.

```bash
hadoop fs -mkdir /piginput
```

Upload the file to HDFS.

```bash
hadoop fs -put word.txt /piginput
```

Verify the file.

```bash
hadoop fs -ls /piginput
```

Expected output:

```
/piginput/word.txt
```

---

# 4. Start Apache Pig (MapReduce Mode)

Run Pig normally.
When Hadoop is running, Pig automatically runs in **MapReduce mode**.

```bash
pig
```

Pig prompt will appear:

```
grunt>
```

---

# 5. Load Data from HDFS

```pig
A = LOAD '/piginput/word.txt' USING PigStorage(' ') AS (line:chararray);
```

### Relation A

Pig reads each line as a single tuple.

```
(hello hadoop)
(hello big data)
(hadoop big data)
```

---

# 6. Tokenize Words

```pig
B = FOREACH A GENERATE FLATTEN(TOKENIZE(line)) AS word;
```

### Relation B

`TOKENIZE` splits each line into words.
`FLATTEN` converts them into individual tuples.

```
(hello)
(hadoop)
(hello)
(big)
(data)
(hadoop)
(big)
(data)
```

---

# 7. Group Words

```pig
C = GROUP B BY word;
```

### Relation C

Pig groups identical words together.

```
(big,{(big),(big)})
(data,{(data),(data)})
(hadoop,{(hadoop),(hadoop)})
(hello,{(hello),(hello)})
```

Format:

```
(word,{all tuples containing that word})
```

---

# 8. Count Words

```pig
D = FOREACH C GENERATE group, COUNT(B);
```

### Relation D

Pig counts the number of occurrences of each word.

```
(big,2)
(data,2)
(hadoop,2)
(hello,2)
```

---

# 9. Store Output in HDFS

```pig
STORE D INTO '/pigoutput';
```

---

# 10. View Output

Exit Pig and check output from HDFS.

```bash
hadoop fs -cat /pigoutput/part-r-00000
```

### Final Output

```
(big,2)
(data,2)
(hadoop,2)
(hello,2)
```

---

# Pig Processing Flow

```
LOAD → TOKENIZE → GROUP → COUNT → STORE/DUMP
```

1. **LOAD** – Reads input data from HDFS
2. **TOKENIZE** – Splits lines into words
3. **GROUP** – Groups identical words
4. **COUNT** – Counts word frequency
5. **STORE** – Saves result in HDFS

---

# Result

The Apache Pig program successfully counts the **frequency of each word** from the dataset stored in **HDFS using Hadoop MapReduce**.
