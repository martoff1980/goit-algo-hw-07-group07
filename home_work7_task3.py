
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


def sum_values_node_right(node, sum_r=0):
    current = node
    if (current.left is None) and (current.right is None):
        sum_r += current.val
        return sum_r

    if current:
        sum_r += current.val
        if current.right:
            if (current.left):
                if sum_r != current.val:
                    sum_r += current.left.val
                return sum_values_node_right(current.right, sum_r)

            if current.left is None:
                return sum_values_node_right(current.right, sum_r)

        if current.right is None:
            return sum_values_node_right(current.left, sum_r)


def sum_values_node_left(node, sum_l=0):
    current = node
    if (current.left is None) and (current.right is None):
        sum_l += current.val
        return sum_l

    if current:
        sum_l += current.val
        if current.right:
            if (current.left):
                if sum_l == current.val:
                    sum_l += current.left.val
                return sum_values_node_left(current.right, sum_l)

            if current.left is None:
                return sum_values_node_left(current.right, sum_l)

        if current.right is None:
            return sum_values_node_left(current.left, sum_l)


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

result_right = sum_values_node_right(root)
result_left = sum_values_node_left(root.left)
result = result_left+result_right
print("Загальна сумма значень:", result)
