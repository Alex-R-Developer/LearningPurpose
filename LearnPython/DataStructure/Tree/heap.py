from heapify import *

class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap)-1)

    def extract_max(self):
        swap(self.heap, 1, len(self.heap) - 1)
        max_value = self.heap.pop()
        heapify(self.heap, 1, len(self.heap))
        return max_value

    def __str__(self):
        return str(self.heap)