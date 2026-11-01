class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def search(root, key):
    if not root:
        return False
    if root.val == key:
        return True
    return search(root.left, key) if key < root.val else search(root.right, key)

# Test
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

key = 40
print(f"Key {key} found:", search(root, key))