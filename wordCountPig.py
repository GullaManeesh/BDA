1️⃣ Create Input File
nano word.txt

Example content:

hello hadoop
hello big data
hadoop big data

Save:

Ctrl + O
Enter
Ctrl + X

Check:

cat word.txt
2️⃣ Start Pig in Local Mode
pig -x local

You will see:

grunt>
3️⃣ Load File
A = LOAD 'word.txt' USING PigStorage(' ') AS (word:chararray);
4️⃣ Group Words
B = GROUP A BY word;
5️⃣ Count Words
C = FOREACH B GENERATE group, COUNT(A);
6️⃣ Display Output
DUMP C;

Output:

hello 2
hadoop 2
big 2
data 2
Full Local Execution (Exam Quick Run)
pig -x local

Inside Pig:

A = LOAD 'word.txt' USING PigStorage(' ') AS (word:chararray);
B = GROUP A BY word;
C = FOREACH B GENERATE group, COUNT(A);
DUMP C;
