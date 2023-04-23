class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        iterator = self.head

        for i in range(index):
            iterator = iterator.next
        
        return iterator

    def find_node_with_data(self, data):
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None 

    def prepend(self, data):
            new_node = Node(data)
            
            if self.head is None:
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                    
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        new_node = Node(data)

        if previous_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else:
            new_node.prev = previous_node 
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def pop_left(self):
        data = self.head.data
    
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
    
        return data

    def pop_right(self):
        data = self.tail.data
    
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
    
        return data

    def delete(self, node_to_delete):
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None
    
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
    
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
    
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
    
        return node_to_delete.data

    def __str__(self):
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str