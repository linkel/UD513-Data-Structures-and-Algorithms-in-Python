class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        def insertNode(node, new_value):
            if new_value < node.value and node.left == None:
                node.left = Node(new_val)
            elif new_value > node.value and node.right == None:
                node.right = Node(new_val)
            elif node.value > new_val and node.left:
                insertNode(node.left, new_value)
            elif node.value < new_val and node.right:
                insertNode(node.right, new_value)
        insertNode(self.root, new_val)

    def printSelf(self):
        def printNode(node):
            if node:
                print(node.value)
                printNode(node.left)
                printNode(node.right)
        printNode(self.root)
        
    def search(self, find_val):
        def preorder(node, find_value):
            if node:
                if node.value == find_value:
                    return True
                return preorder(node.left, find_value) or preorder(node.right, find_value)
            return False
        return preorder(self.root, find_val)

# Kind of wondering how insertion works if you have to rearrange order in the tree.
# This problem didn't check for any of that.

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

#tree.printSelf()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)