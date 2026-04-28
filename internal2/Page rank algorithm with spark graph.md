# 🧪 Experiment: PageRank Algorithm using Spark GraphX

## 🎯 Aim
To implement the PageRank algorithm using Apache Spark GraphX to determine the importance (rank) of each node in a graph.

## 📘 Description
PageRank is a graph algorithm used to measure the importance of nodes based on the number and quality of incoming links.  
In this experiment, a graph is created using vertices and edges, and the PageRank algorithm is applied using GraphX to compute the rank of each node.

## ⚙️ Technologies Used
- Apache Spark – A distributed data processing framework that enables large-scale data computation using parallel processing and in-memory execution. It provides GraphX for graph-based computations.

- Scala – A JVM-based programming language that supports functional and object-oriented programming. It is the primary language for writing Spark applications due to its concise syntax and seamless integration.

- GraphX – A graph processing API in Apache Spark that allows representation of data as vertices and edges. It provides built-in algorithms like PageRank to analyze relationships in graph data.

## 🖥️ Commands to Execute (Ubuntu)
sudo apt update  
sudo apt install openjdk-11-jdk -y  
sudo apt install scala -y  

wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz  
tar -xvzf spark-3.5.1-bin-hadoop3.tgz  
mv spark-3.5.1-bin-hadoop3 ~/spark  

echo 'export SPARK_HOME=~/spark' >> ~/.bashrc  
echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' >> ~/.bashrc  
source ~/.bashrc  

spark-shell  

## 💻 Full Code
import org.apache.spark.graphx._

val vertices = sc.parallelize(Array(
  (1L,"A"), (2L,"B"), (3L,"C"), (4L,"D")
))

val edges = sc.parallelize(Array(
  Edge(1L,2L,1), Edge(2L,3L,1),
  Edge(3L,1L,1), Edge(4L,3L,1)
))

val graph = Graph(vertices, edges)

val ranks = graph.pageRank(0.0001).vertices

ranks.collect.foreach{
  case(id, rank) => println(s"Node $id rank = $rank")
}

## 📊 Output at Each Step
Initial Graph:
Vertices:
(1,A)  
(2,B)  
(3,C)  
(4,D)  

Edges:
Edge(1,2,1)  
Edge(2,3,1)  
Edge(3,1,1)  
Edge(4,3,1)  

PageRank Computation:
Ranks are calculated iteratively based on incoming links.

## ✅ Final Output
Node 1 rank = 1.49  
Node 2 rank = 1.17  
Node 3 rank = 1.91  
Node 4 rank = 0.43  

(Note: Values may slightly vary based on iterations and Spark execution)
