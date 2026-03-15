1️⃣ Start Hadoop
start-dfs.sh
start-yarn.sh
jps

Check services:
You should see

NameNode
DataNode
ResourceManager
NodeManager
2️⃣ Create Input File
nano word.txt

Example content:

hello hadoop
hello big data
hadoop big data

Save:

Ctrl + O
Enter
Ctrl + X
3️⃣ Upload File to HDFS

Create folder:

hadoop fs -mkdir /piginput

Upload file:

hadoop fs -put word.txt /piginput

Check:

hadoop fs -ls /piginput
4️⃣ Start Pig
pig

Pig prompt will appear:

grunt>
5️⃣ Load Data
A = LOAD '/piginput/word.txt' USING PigStorage(' ') AS (word:chararray);
6️⃣ Group Words
B = GROUP A BY word;
7️⃣ Count Words
C = FOREACH B GENERATE group, COUNT(A);
8️⃣ Display Output
DUMP C;

Example output:

hello 2
hadoop 2
big 2
data 2
