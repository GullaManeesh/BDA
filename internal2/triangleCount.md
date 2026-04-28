# 🧪 Experiment: Triangle Count using Apache Spark GraphX

## 🎯 Aim
To compute the number of triangles passing through each vertex in a graph using Apache Spark GraphX.

## 📘 Description
Triangle Count is a graph algorithm used to detect closed triplets (triangles) in a graph.  
A triangle exists when three vertices are mutually connected. In this experiment, GraphX counts how many triangles each node is part of.

## ⚙️ Technologies Used
- Apache Spark – A distributed data processing framework that supports large-scale graph computations through GraphX.

- Scala – A JVM-based programming language used for writing Spark programs with concise and efficient syntax.

- GraphX – A Spark API for graph analytics that provides built-in algorithms like Triangle Count for detecting relationships in graph data.

## 🖥️ Commands to Execute (Ubuntu)

spark-shell  

## 💻 Full Code
import org.apache.spark.graphx._

val edges = sc.parallelize(Array(
  Edge(1L,2L,1),
  Edge(2L,3L,1),
  Edge(3L,1L,1),
  Edge(3L,4L,1)
))

val graph = Graph.fromEdges(edges, 1)

val tri = graph.triangleCount().vertices

tri.collect.foreach{
  case(id, count) => println(s"Node $id -> Triangles $count")
}

## 📊 Output at Each Step
Graph Structure:
Edges:
Edge(1,2,1)  
Edge(2,3,1)  
Edge(3,1,1)  
Edge(3,4,1)  

Triangle Formation:
Nodes 1,2,3 form one triangle  
Node 4 is not part of any triangle  

## ✅ Final Output
Node 1 -> Triangles 1  
Node 2 -> Triangles 1  
Node 3 -> Triangles 1  
Node 4 -> Triangles 0  
