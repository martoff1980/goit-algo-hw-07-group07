class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.sum = 0
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)

        else:
            root.right = insert(root.right, key)

    return root


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

result = min_value_node(root)
print("Мінімальне значення:", result.val)
