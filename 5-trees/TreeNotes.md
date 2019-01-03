### Trees

Trees are like linked lists except they can have more than one next. 

- Trees must be completely connected
- Trees must not have cycles

The level of a tree starts counting at 1 from the root node.
The height of a tree starts counting from the leaf nodes as 0, upwards.
The depth of a tree is the number of edges (connections), which starts at 0 from the root node.

Identical terms:
- Parent/Child
- Ancestor/Descendent
- Internal/Leaf

### Quiz

        a
      /   \
     b     c
    /    / 
   d   e   
         \ 
           f

Level of D?  3
Parent of C? A
Height of B? 2
Depth of F?  3

### Tree Traversal

DFS - depth first search, can be
- preorder: root, L, R
- inorder: L, root, R
- postorder: L, R, root (commonly used for deleting)

BFS - breadth first search, popularly
- search by level, left to right each level

### Quiz

        a
      /   \
     b     c
    / \   
   d   e   
         \ 
           f

Write out the post order traversal.
D, F, E, B, C, A

### Binary Trees

Each node can have at most 2 children. 

**Searching:**
Any of the DFS or BFS traversals work here. O(n), having to look through til found.

**Deleting:**
Often starts off with a search to find the thing to delete.
When deleting, have to consider the children if you delete an internal node (parent).
If it's got one kid, you can just promote the kid up. 
If it's got two, you will have to decide how to shift around the elements. You can search til you hit a leaf and promote the leaf up if you don't care about order. 

**Inserting:**
If there's no order, just stick it in as a child somewhere. Move down tree from root looking for an open spot.
Worse case is O(height). What's the height of the binary tree?

A perfect tree has all children for every parent til the even leaf nodes at the end. Perfect trees have nodes equal to 2^(level-1). 

Powers of 2 remind us of log(n). 
