# 🧪 Experiment: Connected Components using Apache Spark GraphX

## 🎯 Aim
To identify connected components in a graph using Apache Spark GraphX.

## 📘 Description
Connected Components is a graph algorithm used to find groups of vertices that are connected to each other.  
In this experiment, a graph is created using vertices and edges, and GraphX computes components where each node is assigned a component ID representing its group.

## ⚙️ Technologies Used
- Apache Spark – A distributed data processing framework that enables large-scale parallel computation and provides GraphX for graph analytics.

- Scala – A JVM-based programming language used to write Spark applications, offering concise syntax and strong support for functional programming.

- GraphX – A Spark API for graph processing that supports operations on vertices and edges and provides built-in algorithms like Connected Components.

## 🖥️ Commands to Execute (Ubuntu)

spark-shell  

## 💻 Full Code
import org.apache.spark.graphx._

val vertices = sc.parallelize(Array(
  (1L,"A"), (2L,"B"), (3L,"C"),
  (4L,"D"), (5L,"E")
))

val edges = sc.parallelize(Array(
  Edge(1L,2L,1), Edge(2L,3L,1),
  Edge(4L,5L,1)
))

val graph = Graph(vertices, edges)

val cc = graph.connectedComponents().vertices

cc.collect.foreach{
  case(id, comp) => println(s"Node $id -> Component $comp")
}

## 📊 Output at Each Step
Initial Graph:
Vertices:
(1,A)  
(2,B)  
(3,C)  
(4,D)  
(5,E)  

Edges:
Edge(1,2,1)  
Edge(2,3,1)  
Edge(4,5,1)  

Connected Components:
Nodes 1,2,3 belong to one component  
Nodes 4,5 belong to another component  

## ✅ Final Output
Node 1 -> Component 1  
Node 2 -> Component 1  
Node 3 -> Component 1  
Node 4 -> Component 4  
Node 5 -> Component 4  

(Note: Component IDs may vary but grouping remains same)
