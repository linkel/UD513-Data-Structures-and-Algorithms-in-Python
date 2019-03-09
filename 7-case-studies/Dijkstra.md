### Shortest Path Problem

The shortest path in an unweighted graph is just the path with the fewest number of edges. This is a breadth first search, and whichever one you find first is the shortest one. 

### Dijkstra's Algorithm

Example is for a weighted graph. 

Greedy algorithm that uses a min priority queue to extract the minimum, queue up paths to other nodes with info on how long they take. Node info gets updated with the lowest path if another lower one is found. 

Adjacency matrix representation of this weighted graph example:

  U D A C I T Y
U 0 3 4 6 0 0 0
D 3 0 0 4 0 0 0 
A 4 0 0 0 7 0 0 
C 6 4 0 0 4 0 0 
I 0 4 7 4 0 0 4
T 0 0 0 0 0 0 5
Y 0 0 0 0 4 5 0

Dijkstra's algo calculation by step

U D A C I T Y
0 inf -------->
x 3 4 6 inf---->
x x 4 6 inf ---->
x x x 6 11 inf -->
x x x x 10 11 inf
x x x x x 11 14
x x x x x x 14


