class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def pre_order_traverse(node):
        print(node.data)
        pre_order_traverse(node.left_child)
        pre_order_traverse(node.right_child)

    def post_order_traverse(node):
        post_order_traverse(node.left_child)
        post_order_traverse(node.right_child)
        print(node.data)

    def in_order_traverse(node):
        in_order_traverse(node.left_child)
        print(node.data)
        in_order_traverse(node.right_child)

class FullBinaryTree:
    def get_parent_index(complete_binary_tree, index):
        parent_index = index // 2

        if 0 < parent_index < len(complete_binary_tree):
            return parent_index

        return None

    def get_left_child_index(complete_binary_tree, index):
        left_child_index = 2 * index

        if 0 < left_child_index < len(complete_binary_tree):
            return left_child_index

        return None

    def get_right_child_index(complete_binary_tree, index):
        right_child_index = 2 * index + 1

        if 0 < right_child_index < len(complete_binary_tree):
            return right_child_index

        return None

