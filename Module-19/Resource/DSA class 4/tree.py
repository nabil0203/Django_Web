class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Manually construct the binary tree
# Example Tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# DFS Traversals
def inorder(node):
    if node: #1/2/4/5/3/6
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def preorder(node):
    if node: #1/2/4/5/3/6
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node: #4/5/2/6/3/1
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

# Function to count leaf nodes
def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


# Testing
print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
print("\nLevel-order Traversal:")
print(f"\nNumber of leaf nodes: {count_leaves(root)}")
