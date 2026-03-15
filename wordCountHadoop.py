# Word Count using Hadoop Streaming (Python MapReduce)

## Objective

To implement **Word Count using Hadoop MapReduce with Python (Hadoop Streaming)**.
The program counts how many times each word appears in a text file.

---

# 1. Start Hadoop Services

Start Hadoop Distributed File System and YARN.
in desktop
```bash
sh own.sh
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

# 3. Create Mapper Program

Create mapper file.

```bash
nano mapper.py
```

### Mapper Code

```python
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    words = line.strip().split()

    for word in words:
        print(f"{word}\t1")
```

### Mapper Explanation

The mapper:

1. Reads input line by line
2. Splits each line into words
3. Emits key-value pair

```
Word → Key
1 → Value
```

### Mapper Output Example

```
this    1
is      1
a       1
demo    1
this    1
ia      1
a       1
hadoop  1
file    1
hadoop  1
is      1
big     1
```

---

# 4. Create Reducer Program

Create reducer file.

```bash
nano reducer.py
```

### Reducer Code

```python
#!/usr/bin/env python3

import sys

current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split()
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(current_word, current_count)
        current_word = word
        current_count = count

if current_word:
    print(current_word, current_count)
```

### Reducer Explanation

The reducer:

1. Receives sorted mapper output
2. Groups identical words
3. Adds counts of each word
4. Prints total occurrences

---

# 5. Test Mapper and Reducer Locally

Before running Hadoop, test locally.

```bash
cat word.txt | python3 mapper.py | sort -k1,1 | python3 reducer.py
```

### Output

```
a 2
big 1
demo 1
file 1
hadoop 2
ia 1
is 2
this 2
```

Explanation:

```
a → 2 occurrences
hadoop → 2 occurrences
is → 2 occurrences
this → 2 occurrences
```

---

# 6. Upload File to HDFS

Create directory in HDFS.

```bash
hadoop fs -mkdir /wordcount
```

Upload dataset.

```bash
hadoop fs -put word.txt /wordcount
```

Verify upload.

```bash
hadoop fs -ls /wordcount
```

Expected output:

```
/wordcount/word.txt
```

---

# 7. Give Execution Permission

```bash
chmod +x mapper.py
chmod +x reducer.py
```

---

# 8. Run Hadoop Streaming Job

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file mapper.py \
-mapper mapper.py \
-file reducer.py \
-reducer reducer.py \
-input /wordcount/word.txt \
-output /wordcount_output
```

---

# 9. Check Output Directory

```bash
hadoop fs -ls /wordcount_output
```

Output

```
part-00000
_SUCCESS
```

---

# 10. View Final Output

```bash
hadoop fs -cat /wordcount_output/part-00000
```

### Final Output

```
a 2
big 1
demo 1
file 1
hadoop 2
ia 1
is 2
this 2
```

---

# MapReduce Processing Flow

```
Input File
     ↓
Mapper → (word,1)
     ↓
Shuffle & Sort
     ↓
Reducer → Sum of counts
     ↓
Output
```

---

# Result

The Hadoop MapReduce program successfully counts the **frequency of each word** in the input dataset using **Python mapper and reducer scripts with Hadoop Streaming**.
