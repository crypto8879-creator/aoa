class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_total(root):
    if not root:
        return 0
    return 1 + count_total(root.left) + count_total(root.right)

def count_leaf(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaf(root.left) + count_leaf(root.right)

def count_internal(root):
    if not root or (not root.left and not root.right):
        return 0
    return 1 + count_internal(root.left) + count_internal(root.right)

# Test
root = Node(1)
root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right = Node(4), Node(5)
root.right.right = Node(6)

print("Total Nodes:", count_total(root))
print("Leaf Nodes:", count_leaf(root))
print("Internal Nodes:", count_internal(root))