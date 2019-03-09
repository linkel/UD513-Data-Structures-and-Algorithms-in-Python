### Eulerian and Hamiltonian Paths and Cycles

The lecturer sort of switched back and forth between saying paths and cycles and didn't emphasize vertices vs edges hard enough, which was kind of annoying and confusingly inconsistent. 

Basically, a Eulerian (pronounced Oilerian) path visits every EDGE exactly one time, starting and ending anywhere. A Eulerian cycle visits every EDGE exactly one time, starting and ending at the same node.

A Hamiltonian path visits every NODE (VERTEX) exactly one time, starting and ending anywhere. A Hamiltonian cycle visits every NODE exactly one time, starting and ending at the same node.

### Algo for Eulerian

Possible algo for finding Eulerian paths is:

1. Start at any vertex and follow edges until you return back to that vertex.
2. If you haven't yet seen every edge, then do an unseen edge connected to the node you already visited. Do the same thing.
3. Once you have seen every edge, combine the paths at the nodes that they have in common.

O(# of edges)
