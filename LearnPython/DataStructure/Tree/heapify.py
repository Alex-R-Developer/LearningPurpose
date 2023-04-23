def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index

    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, tree_size)


def reverse_heapify(tree, index):
    parent_index = index // 2

    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)
        reverse_heapify(tree, parent_index)      


def heapsort(tree):
    tree_size = len(tree)

    for index in range(tree_size-1, 0, -1):
        heapify(tree, index, tree_size)

    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)