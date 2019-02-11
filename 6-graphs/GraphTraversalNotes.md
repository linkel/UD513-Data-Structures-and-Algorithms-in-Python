### Graph Traversal
Travelling along a graph is kind of like travelling along a tree, except that there is no root node and paths can loop back to each other. So most of these methods make use of flagging a node as previously seen.

Searching a graph and travelling a graph are also quite similar--with searching a graph you want to stop when you find the item you were looking for and with travelling, you'd keep going through all of them til there were no more to go through. 

### Depth First Search
In a DFS, you travel all the way down one path til there's no more and then will retrace. Iterative implementation of this may use a stack, where nodes are loaded onto the stack and marked as seen, and when you hit the end of one path you'd pop a node off the stack to go back to it and traverse any edges on that one. 

Can also be written recursively where the base case is one where there are no more nodes to explore on a path, and you go back up a level of recursion to keep looking. 

### Breadth First Search
In a BFS, you travel all the edges connected to the one that you're on before you travel the edges of each one of those next nodes. It's like going by levels, which makes it kind of like turning a graph into a tree. You can use a queue for this, where you mark nodes as seen and when you finish all the edges of the node you are at (queuing all the way), you then peel the next one out of the queue and traverse the levels for that node.

