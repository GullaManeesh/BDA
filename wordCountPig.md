# Word Count using Apache Pig

## Objective

To perform **Word Count** using **Apache Pig** and understand how Pig Latin processes data step by step.

---

# 1. Start Hadoop Services

Start Hadoop Distributed File System and YARN.

```bash
start-dfs.sh
start-yarn.sh
jps
```

### Verify Running Services

You should see the following processes:

```
NameNode
DataNode
ResourceManager
NodeManager
```

---

# 2. Create Input File

Create a sample text file.

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

# 3. Start Apache Pig

Run Pig in local mode.

```bash
pig -x local
```

You will see the Pig prompt:

```
grunt>
```

---

# 4. Load Data

```pig
A = LOAD 'word.txt' USING PigStorage(' ') AS (line:chararray);
```

### Relation A

Pig reads each line as a single tuple.

```
(hello hadoop)
(hello big data)
(hadoop big data)
```

---

# 5. Tokenize Words

```pig
B = FOREACH A GENERATE FLATTEN(TOKENIZE(line)) AS word;
```

### Relation B

`TOKENIZE` splits each line into words and
`FLATTEN` converts them into separate tuples.

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

# 6. Group Words

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

**Format**

```
(word,{all tuples containing that word})
```

---

# 7. Count Words

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

# 8. Display Output

```pig
DUMP D;
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
LOAD → TOKENIZE → GROUP → COUNT → DUMP
```

1. **LOAD** – Reads input file
2. **TOKENIZE** – Splits lines into words
3. **GROUP** – Groups identical words
4. **COUNT** – Counts occurrences
5. **DUMP** – Displays result

---

# Result

The Apache Pig program successfully counts the frequency of each word in the input dataset.
