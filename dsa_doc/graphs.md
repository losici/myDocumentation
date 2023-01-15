# Graphs
Data structure to show relationship between object.
A graph is like a network, where the nodes or verteces are connected by edges. A tree is just a type of graph.
Graphs don't have a root. Nodes store data, edges are connections but they can actrually store data too.

## Directions and Cycles
Edges can have a direction, meaning the relationship between two nodes only applies one way. This is also called **Directed graph**. If you have opposite directions, you have two edges between the same two nodes one representing each direction you travel in. An **Undirected graph** has edges without directions.<br/>
Graphs can have **cycles**. A cycle start when you start from one node and you follow all the edsge alla the way back to that node. If you have a cycle you might go to an infinite loop! Always be sure that your input has no cycles. A typical example og graph is **DAG**: Directed, Acyclic Graph = a directed graph with no cyles.

## Connectivity
1. Disconnected: Disconnected graphs are very similar whether the graph's directed or undirected, there is some vertex or group of vertices that have no connection with the rest of the graph. Practically speaking it has a node with no edges or that it is separated from other verteces.
1. Weakly Connected: A **directed** graph is weakly connected when only replacing all of the directed edges with undirected edges can cause it to be connected. Imagine that your graph has several vertices with one outbound edge, meaning an edge that points from it to some other vertex in the graph. There's no way to reach all of those vertices from any other vertex in the graph, but if those edges were changed to be undirected all vertices would be easily accessible.
1. Connected graph: Here we only use "connected graph" to refer to **undirected** graphs. In a connected graph, there is some path between one vertex and every other vertex. There is no vertex disconnected.
1. Strongly Connected: Strongly connected directed graphs must have a path from every node and every other node. So, there must be a path from A to B AND B to A. <br/>
### What is connectivity?
Let's look at the image below.
![graphs_connectivity.png](/dsa_doc/imgs/graphs_connectivity.png "graphs_connectivity.png")<br/>
If you remove one connection to the graph on the left you have disconnected graph. Which is not the same for the graph on the right.
Coonectivity is the minimum number of elements that need to be removed for a graph to become disconnected. Depending on the information on the graph you can use connectivity to answer the question which graph is stronger.

# How to represent a Graph?
There are three methods and they will be listed below.

## Edge Lists
An edge list is a list of edges. The edges are represented by a 
list of two elements.  Those elements are normally numbers that correspond to ID numbers for vertices.
![edge_list.png](/dsa_doc/imgs/edge_list.png "edge_list.png")<br/>
An edge list is a 2D list.

## Adjancency List
It is another way to display a graph.<br/>
![graphs_Adjancency_list.png](/dsa_doc/imgs/graphs_Adjancency_list.png "graphs_Adjancency_list.png")<br/>
The verteces have an ID number which corresponds to the index of the array. In the array there the IDs of the other vertices to which the index-vertex is connected to. 

## Adjacency Matrix
In computer science a matrix is a 2D array but the lists inside are all the same lentgh. A matrix can also be called a rectangular matrix. The rows and col indeces represent the verteces with those IDs. The ineer lists represent the connections and they can be 1 o 0 depending if the connection there is or not.<br/>
In general:
- 0 means no edges
- 1 means there is an edge
The diagonal is always zero unless a node has an edge that goes on itself. Moreover the connections will appear twice in the matrix (to be honest we could look just at the triangular matrix for an undirected graph).<br/>
![graph_adjancency_matrix.png](/dsa_doc/imgs/graph_adjancency_matrix.png "graph_adjancency_matrix.png")<br/>

# Graph Traversal
Graph traversal: you look in every element.<br/>
Graph search: you stop traversing when you find the element.<br/>
## DFS
You can begin with every node. Mark the node you selected as **seen**. A common implementation is to use a **stack**.<br/>
You add the node in the Seen as long you go, and then the vertex in the stack. If you encounter a node that you have already seen you go back to the previous node and try another edge. If you run out of edges then you pop the node from the stack and go to the one before, which is  the next one in the stack. You continue this approach until you pop everything off (LIFO) from the stack or you find the node you were looking for.<br/>
Runtime = O(|E|+|V|) you visit each vertex and edge.<br/>
The number of edges summarize the runtime very well.<br/>
### Summary DFS
- stack
- you explore first vertically
- 

The rough algorithm for DFS can be thought of as the following:

1. Start at s. It has distance 0 from itself.
1. Consider a node adjacent to s. Call it t. It has distance 1. Mark it as visited.
1. Then consider a node adjacent to t that has not yet been visited. It has distance 2. Mark it as visited.
1. Repeat until all nodes reachable from s﻿ are visited.
## BFS
It is similar to DFS, you visit every edges and you mark every node. Here the implementation is with a **queue**.
You mark the first as a seen, we go to the next one and we add it to the queue (FIFO). You dequeue when you run out of edges. When we dequeue we get a node adjacent to the one that we started with. You can envision a BSF like a tree out of a graph. We need to continue adding nodes one level at a time. We finish off one level entirely before moving on to the next.<br>
Runtime = O(|E|+|V|) you visit each vertex and edge.<br/>

### Summary BFS
- breadth = broad/wide
- the algorithm first move horizontally and then vertically
- the algorithm uses a queue
- BFS is the algorithm to use if we want to find the shortest path in an **undirected, unweighted graph**. The claim for BFS is that the first time a node is discovered during the traversal, that distance from the source would give us the shortest path.
The rough algorithm for BFS can be thought of as the following:

1. Begin at the starting node s. It has distance 0 from itself.
1. Consider nodes adjacent to s. They have distance 1. Mark them as visited.
1. Then consider nodes that have not yet been visited that are adjacent to those at distance 1. They have distance 2. Mark them as visited.
1. Repeat until all nodes reachable from s are visited.

## Comparison BFS and DFS
Both DFS and BFS have a worst-case time complexity of O(|V| +|E|).<br/>
Notice, however, that, though their worst-case time complexities are the same, their memory management is totally different! In other words, to traverse the graph, BFS had to store all of a vertex's neighbors in each step in a queue to later be able to traverse those neighbors. On the other hand, if you take a look at the recursive implementation of DFS, DFS only needed to store the previous neighbor to explore the next one. As a result, for certain graph structures, DFS can be more memory-efficient.

## Dijkstra's Algorithm
Useful for **weighted graph**.
The idea behind Dijkstra's Algorithm is that we are constantly looking for the **lowest-weight** paths and seeing which vertices are discovered along the way. As a result, the algorithm explores neighbors similarly to how the Breadth First Search algorithm would, except that it prioritizes which neighbors it searches for next by calculating which neighbor lies on the path with the lowest overall path weight.
### Summary
- priority queue: to store the possible paths and uses the total weights of the paths to determine priority.
## Eulerian Paths and Cycles
A path is just a specific route you take in a traversal or search. You could create a path trah travels through every edge in a graph at least once. That path is called Eulerian Path.<br/>
Eulerian Cycle: you have to traverse the edge only once and end in the node where you started. Not every graph is capable to have an Eulerian Path. Graphs can have eulerian cycles if all vertices have an even degree or an even number of edges connected to them. Eulerian Paths are a little bit more lenient. So it's ok for a graph to have two nodes with odd degree as long as they are the start and the end of the path.

### Quick algorithm for Eulerian cycles
You can start on any vertex and follow the edges until you return back to that vertex. If you didn't encounter every edge, you can start from an unseen edge connected to a node you've already visited. Again you create a path through those unseen edges, you can continue this process until you have seen every edge in the graph once. Then you can simply add the paths together, combining them at the nodes they have in common. This algorithm is really efficien O(|E|)

## Hamiltonian Paths
It must go through every vertex at least once. It will start and end with the same vertex.