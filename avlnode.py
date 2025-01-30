class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if root is None:
            return AVLNode(key)
        
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def min_value_node(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.val

    def max_value_node(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.val
    
    def find_summ(self, root):
        if root is None:
            return 0
        return root.val + self.find_summ(root.left) + self.find_summ(root.right)