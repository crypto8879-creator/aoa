class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def iterative_inorder(root):
    stack, curr = [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val, end=" ")
        curr = curr.right

# Test
root = Node(1)
root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right = Node(4), Node(5)

print("Iterative Inorder:")
iterative_inorder(root)
print()