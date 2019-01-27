### Graph

A graph is a network. It has nodes (also known as vertexes) and they are connected by edges. A tree is actually a type of graph!

We might think a node stores data and an edge doesn't, but actually an edge can store data too! 

For example, we could have nodes that represent people, and nodes have a value that is their name. Perhaps the edges that connect them indicate that they met, or that they're in the same city. The edges can contain data baout the strength of their connection--maybe they met and they're great friends, so this edge is worth 6 instead of 2. 

Or maybe the nodes represent airports, and edges indicate how long the flights are or maybe how expensive the flight is. And you could try to minimize the price cost as you navigate through the graph.

### Directions and Cycles

A Directed Graph, or a digraph, is one that has a direction. The edges have arrows that point in one direction. 

An undirected graph is one that points in both directions.

A cycle is when you can start at a node and follow edges all the way back to the node. 

A directed acyclic graph (DAG) is a directed graph with no cycles!

### Connectivity

Connectivity, in Graph Theory, indicates the level of connections between nodes. If I can remove one edge and it breaks the nodes into separate chunks (disconnected graph) then it's less connected than something that can have more edges removed.

A directed graph is weakly connected when only replacing all of the directed edges with undirected edges can cause it to be connected. So if you have a vertex that has an outbound edge but not an inbound edge, and if you replace that edge with a undirected edge it allows connectivity to that vertex, then that graph was weakly connected.

Strongly connected directed graphs have a path from every node to every other node. A to B and B to A. 

### Quiz

Cycles in the provided graph were 3, and it was weakly connected. Odd because I can count 4, so maybe I'm not sure what counts as a cycle?