### Binary Search Trees

The difference is that everything to the left of the root node is smaller than it and everything to its right is bigger.

Searching this tree if it is pretty balanced then is O(log(n)), because it depends on the height of the tree (which in a previous calculation was shown to be log(n)). 

In the worst case, where it is completely unbalanced, it is basically like a line and it would be linear O(n) time. 



I'm kind of curious on how shuffling the tree around works if I make inserts that require that reshuffling. The quiz where the implementation was done did not address this. 