### Heaps
Heaps are unlike binary trees in that they don't have to have 2 children. 

The topmost node (root node) must be either the biggest or the smallest, and then going from left to right in each level, the numbers must descend or ascend appropriately (monotonicity?). Min heap has the root being the smallest and max heap has the root being the biggest. 

They must also be complete, so L to R until filled (don't have to be perfect trees but cannot fill in the right if the left is not done). 

Peeking looks at the top node which is either the largest or the smallest so it takes O(1) time.

Worst case search takes O(n) if what you want is at the end, and average case takes O(n/2) because if you hit a value that is smaller than your searched-for number in a max heap you know you can stop.

### Heapify

Generally when you insert into a heap, convention is to stick the element in the bottom most open leaf and then heapify, which means to sort it properly. 

Extracting works similarly--if you remove the root, then you just take the last one and stick it up top then heapify. 

Heaps can be stored in arrays because one knows that for a heap with two children per node, the array index increases by powers of 2. 

ex: 

Levels: 1 2 2 3 3 3 3