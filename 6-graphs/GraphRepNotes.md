### Edge List

A 2D list that shows a list of edges. It lists the vertices/nodes that are connected to each other. 
[[0,1],[1,2],[1,3],[2,3]]

### Adjacency List

Each node corresponds to an index in an array. 

0      1        2       3
[[1],[0,2,3],[1,3],[1,2]]

### Adjacency Matrix

for each node, 1 if connected, 0 if not neighbors. 
    0  1  2  3
0    [[0,1,0,0],
1    [1,0,1,1],
2    [0,1,0,1],
3    [0,1,1,0]]