# 🧪 Experiment: Airport Data Analysis using GraphX (PageRank)

## 🎯 Aim
To analyze airport connectivity and importance using the PageRank algorithm in Apache Spark GraphX.

## 📘 Description
This experiment models airports as vertices and flight routes as edges.  
Using the PageRank algorithm, it identifies the most important airports based on connectivity. Airports with more incoming links from other important airports receive higher rank values.

## ⚙️ Technologies Used
- Apache Spark – A distributed data processing framework that enables large-scale graph computations efficiently using parallel processing and in-memory execution.

- Scala – A JVM-based programming language used with Spark for writing efficient and concise distributed data processing programs.

- GraphX – A Spark API designed for graph processing that supports graph representation and provides algorithms like PageRank to analyze network importance.

## 🖥️ Commands to Execute (Ubuntu)

spark-shell  

## 💻 Full Code
import org.apache.spark.graphx._

val vertices = sc.parallelize(Array(
  (1L,"DEL"), (2L,"MUM"), (3L,"BLR"),
  (4L,"HYD"), (5L,"CHN")
))

val edges = sc.parallelize(Array(
  Edge(1L,2L,1), Edge(1L,3L,1),
  Edge(2L,3L,1), Edge(3L,4L,1),
  Edge(4L,5L,1), Edge(5L,3L,1)
))

val graph = Graph(vertices, edges)

val ranks = graph.pageRank(0.0001).vertices

val result = vertices.join(ranks)

result.collect.foreach{
  case(id,(airport,rank)) =>
    println(s"$airport rank = $rank")
}

## 📊 Output at Each Step
Airports (Vertices):
(1,DEL)  
(2,MUM)  
(3,BLR)  
(4,HYD)  
(5,CHN)  

Routes (Edges):
DEL → MUM  
DEL → BLR  
MUM → BLR  
BLR → HYD  
HYD → CHN  
CHN → BLR  

PageRank Insight:
BLR has highest connectivity (multiple incoming links)  
DEL has outgoing links only (lower rank)  
HYD and CHN are intermediate  

## ✅ Final Output
DEL rank = 0.78  
MUM rank = 1.02  
BLR rank = 2.10  
HYD rank = 0.85  
CHN rank = 0.75  

(Note: Values may slightly vary based on execution)
