class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


def iterative_inorder(root):
    stack, curr = [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val, end=" ")
        curr = curr.right


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


def find_min(root):
    if not root:
        return float('inf')
    return min(root.val, find_min(root.left), find_min(root.right))


def find_max(root):
    if not root:
        return float('-inf')
    return max(root.val, find_max(root.left), find_max(root.right))


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


root = Node(10)
root.left, root.right = Node(5), Node(20)
root.left.left, root.left.right = Node(3), Node(7)
root.right.right = Node(25)

print("Inorder:")
inorder(root)
print("\nPreorder:")
preorder(root)
print("\nPostorder:")
postorder(root)
print("\nIterative Inorder:")
iterative_inorder(root)
print()

print("\nTotal Nodes:", count_total(root))
print("Leaf Nodes:", count_leaf(root))
print("Internal Nodes:", count_internal(root))
print("Min Value:", find_min(root))
print("Max Value:", find_max(root))

bst_root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst_root = insert(bst_root, val)

key = 40
print(f"\nSearch {key} in BST:", search(bst_root, key))