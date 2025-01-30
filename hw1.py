class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return AVLNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def max_value_node(root):
    if root is None:
        return None  
    current = root
    while current.right is not None:
        current = current.right
    return current.val


root = AVLNode(5)
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)

print(root)

max_value = max_value_node(root)
if max_value is not None:
    print(f"Max: {max_value}")