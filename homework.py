import avlnode

def main():
    avl = avlnode.AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl.insert(root, key)

    print("Min Value:", avl.min_value_node(root))
    print("Max Value:", avl.max_value_node(root))

    print("Sum of all nodes:", avl.find_summ(root))

if __name__ == "__main__":
    main()