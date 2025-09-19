# Class 4: Binary Trees

**Duration:** 90 minutes

## Topics to Discuss
- Tree terminology: root, leaf, depth, height
- Binary Tree and traversals: inorder, preorder, postorder, level-order
- Tree representation in Python

## Activities
- Construct binary tree manually and traverse using recursion
- Visualize tree structure using print statements

## Binary Tree Basics

**Terminology:**  
- **Root:** Topmost node of the tree  
- **Leaf:** Node with no children  
- **Depth:** Distance from root to a node  
- **Height:** Length of the longest path from a node to a leaf  

**Traversals:**  
1. **Inorder (Left → Root → Right)**  
2. **Preorder (Root → Left → Right)**  
3. **Postorder (Left → Right → Root)**  
4. **Level-order (Breadth-first)**

## Python Implementation

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

# BFS Traversal (Level-order)
from collections import deque

def level_order(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

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
level_order(root)
print(f"\nNumber of leaf nodes: {count_leaves(root)}")
