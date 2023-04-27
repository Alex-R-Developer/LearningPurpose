class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap)-1)

    def extract_min(self):
        swap(self.heap, 1, len(self.heap) - 1)
        min_value = self.heap.pop()
        heapify(self.heap, 1, len(self.heap))
        return min_value[1]

    def __str__(self):
        return str(self.heap)


def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapify(tree, index, tree_size):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    smallest = index

    if 0 < left_child_index < tree_size and tree[smallest] > tree[left_child_index]:
        smallest = left_child_index

    if 0 < right_child_index < tree_size and tree[smallest] > tree[right_child_index]:
        smallest = right_child_index
        
    if smallest != index:
        swap(tree, index, smallest)
        heapify(tree, smallest, tree_size)

def reverse_heapify(tree, index):
    parent_index = index // 2

    if 0 < parent_index < len(tree) and tree[index] < tree[parent_index]:
        swap(tree, index, parent_index)
        reverse_heapify(tree, parent_index)      


def heapsort(tree):
    tree_size = len(tree)

    for index in range(tree_size-1, 0, -1):
        heapify(tree, index, tree_size)

    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)