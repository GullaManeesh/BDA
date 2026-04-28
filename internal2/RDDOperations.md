# 🧪 Experiment: Demonstrate RDD Operations (Map, Filter, FlatMap, Graph)

## 🎯 Aim
To demonstrate the working of Apache Spark RDD operations: Map, Filter, FlatMap, and Graph (GraphX).

## 📘 Description
This experiment uses Apache Spark to perform transformations on distributed data (RDD).  
Map transforms each element, Filter selects elements based on condition, FlatMap splits and flattens data, and GraphX is used to represent graph data using vertices and edges.

## ⚙️ Technologies Used
- Apache Spark – Distributed data processing framework  
- Scala – Programming language for Spark  
- GraphX – API for graph processing  
- Ubuntu – Operating system  

## 🖥️ Commands to Execute (Ubuntu)

spark-shell  

## 💻 Full Code
val data = sc.parallelize(List(1,2,3,4,5))

// MAP
val mapRes = data.map(x => x * 2)
mapRes.collect().foreach(println)

// FILTER
val filterRes = data.filter(x => x % 2 == 0)
filterRes.collect().foreach(println)

// FLATMAP
val words = sc.parallelize(List("hello spark", "big data"))
val flatRes = words.flatMap(x => x.split(" "))
flatRes.collect().foreach(println)

// GRAPH (GraphX)
import org.apache.spark.graphx._

val vertices = sc.parallelize(Array(
  (1L, "A"), (2L, "B"), (3L, "C")
))

val edges = sc.parallelize(Array(
  Edge(1L,2L,1), Edge(2L,3L,1)
))

val graph = Graph(vertices, edges)

graph.vertices.collect.foreach(println)
graph.edges.collect.foreach(println)

## 📊 Output at Each Step
MAP OUTPUT:
2  
4  
6  
8  
10  

FILTER OUTPUT:
2  
4  

FLATMAP OUTPUT:
hello  
spark  
big  
data  

GRAPH VERTICES:
(1,A)  
(2,B)  
(3,C)  

GRAPH EDGES:
Edge(1,2,1)  
Edge(2,3,1)  

## ✅ Final Combined Output
2  
4  
6  
8  
10  
2  
4  
hello  
spark  
big  
data  
(1,A)  
(2,B)  
(3,C)  
Edge(1,2,1)  
Edge(2,3,1)  
