### Red Black Trees

Example of a self-balancing tree. Red black trees are a type of BST (binary search tree) with extra rules.

1. Root node must be black (sometimes optional rule)
2. If a node is red, its two children must be black
3. There exist null leaf nodes that are always black
4. Every path in this tree must have the same # of black nodes. 

Generally, nodes are inserted as red nodes. 

### Tree Rotation

When a parent P of an inserted red node is red while P's sibling is black, one must perform a tree rotation. 

(I'm not adding in the null black nodes for this diagram)

    9b
 /     \
6b      19b
       /   \
    13r     16r

In the example-- left rotation. 

    9b
 /     \
6b      19b
       / 
    16r    
   /
  13r

And we still have to follow the rules of the BST! So while we balance the tree we keep that in mind. Hence we need...a right rotation in order to balance the tree:


    9b
 /     \
6b      16b <--- this got turned black
       /  \
    13r     19r


Gosh, I wish there were more finger exercises for this section. 


