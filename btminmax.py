class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_min(root):
    if not root:
        return float('inf')
    return min(root.val, find_min(root.left), find_min(root.right))

def find_max(root):
    if not root:
        return float('-inf')
    return max(root.val, find_max(root.left), find_max(root.right))

# Test
root = Node(10)
root.left, root.right = Node(5), Node(20)
root.left.left, root.left.right = Node(3), Node(7)
root.right.right = Node(25)

print("Min Value:", find_min(root))
print("Max Value:", find_max(root))