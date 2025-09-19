# Binary Search Trees (BST)

A **Binary Search Tree (BST)** is a type of binary tree where each node satisfies the following properties:

1. **Left subtree** of a node contains values **less than** the node’s value.  
2. **Right subtree** contains values **greater than** the node’s value.  
3. Both left and right subtrees must also be BSTs.  
4. All values in a BST are **unique**.  

> These properties allow **fast searching, insertion, and deletion** compared to a regular binary tree.  

---

## Key Concepts

- **Size of a tree**: Number of nodes (`n`).  
- **Subtree**: A node and all its descendants.  
- **Height of a node**: Maximum number of edges from that node to a leaf.  
- **In-order successor**: Node that comes immediately after a given node during **in-order traversal**.  

---

## Traversal

- **In-order traversal (Left → Root → Right)** produces a **sorted list** of values for a BST.

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

# Example BST
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left, root.right = node7, node15
node7.left, node7.right = node3, node8
node15.left, node15.right = node14, node19
node19.left = node18

# In-order traversal
inOrderTraversal(root)  # Output: 3, 7, 8, 13, 14, 15, 18, 19
```

---

## Searching in BST

- Start at **root**.  
- If value equals node, return node.  
- If value < node → go **left**.  
- If value > node → go **right**.  
- Stop when value is found or `None` is reached.

```python
def search(node, target):
    if node is None:
        return None
    if node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

result = search(root, 13)
print(f"Found: {result.data}" if result else "Not found")
```

- **Time complexity**: O(h)  
  - Balanced tree: O(log n)  
  - Unbalanced tree: O(n)

---

## Insertion in BST

- Similar to searching.  
- Insert as a **leaf node** at the correct position.

```python
def insert(node, data):
    if node is None:
        return TreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node

insert(root, 10)
```

---

## Finding Minimum Value in Subtree

```python
def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

print("Lowest value:", minValueNode(root).data)
```

- Useful for **deletion** (finding in-order successor).

---

## Deletion in BST

Three cases when deleting a node:

1. **Leaf node** → remove node.  
2. **One child** → replace node with child.  
3. **Two children** →
   - Find in-order successor (minimum in right subtree).  
   - Replace node value with successor value.  
   - Delete successor node.

```python
def delete(node, data):
    if not node:
        return None
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if not node.left:  # One or no child
            return node.right
        elif not node.right:
            return node.left
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)
    return node

delete(root, 15)
```

---

## BST vs Other Data Structures

| Data Structure | Search | Insert/Delete |
|----------------|-------|---------------|
| Sorted Array   | O(log n) | Expensive (shifting) |
| Linked List    | O(n)     | Easy (no shift)      |
| BST (balanced) | O(log n) | Easy (no shift)      |

---

## BST Balance and Time Complexity

- Operations depend on **height `h`**:
  - Balanced BST: h ≈ log₂ n → O(log n)  
  - Unbalanced BST: h ≈ n → O(n)

- **Balanced BST** → efficient.  
- **Unbalanced BST** → slower, like a linked list.

> AVL Trees and Red-Black Trees are self-balancing BSTs for optimal performance.
