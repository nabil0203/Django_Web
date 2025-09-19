class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#       13
#      /  \
#     7    15
#    / \   / \
#   3   8 14 19
#             /
#            18

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)


# Traverse
inOrderTraversal(root)


# Search in BST
def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)


# Search for a value
result = search(root, 13)
if result:
    print(f"\nFound the node with value: {result.data}")
else:
    print("Value not found in the BST.")


# Find Minimum in BST
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


print("\nFinding the lowest value in the BST:")
# Traverse
inOrderTraversal(root)

# Find Lowest
print("\nLowest value:", minValueNode(root).data)


# Insert in BST
def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
        return node


# Inserting new value into the BST
insert(root, 10)

# Traverse
print("After inserting 10:")
inOrderTraversal(root)


def delete(node, data):
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if not node.left:
            temp = node.right
            return temp
        elif not node.right:
            temp = node.left
            return temp

        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)

    return node


# Traverse
inOrderTraversal(root)

# Delete node 15
delete(root, 15)

# Traverse
print("\nAfter deleting 15:")
inOrderTraversal(root)
