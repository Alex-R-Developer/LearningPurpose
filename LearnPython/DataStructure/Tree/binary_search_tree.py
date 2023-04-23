class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def find_min(node):
        temp = node
        
        while temp.left_child is not None:
            temp = temp.left_child
        
        return temp

    def search(self, data):
        temp = self.root

        while temp is not None:
            if data == temp.data:
                return temp
                
            if data > temp.data:
                temp = temp.right_child
            else:
                temp = temp.left_child

        return None
            
    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            return
        
        temp = self.root

        while temp is not None:
            if data > temp.data:
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                else:
                    temp = temp.right_child
            elif data < temp.data:
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                else:
                    temp = temp.left_child
            else:
                return

    def delete(self, data):
        node_to_delete = self.search(data)
        parent_node = node_to_delete.parent

        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = None
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = None
            else:
                parent_node.right_child = None

        elif node_to_delete.left_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
            else:
                parent_node.right_child = node_to_delete.right_child
            
            node_to_delete.right_child.parent = parent_node

        elif node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
            else:
                parent_node.right_child = node_to_delete.left_child
            
            node_to_delete.left_child.parent = parent_node
        
        else:
            successor = self.find_min(node_to_delete.right_child)
            node_to_delete.data = successor.data
            
            if successor is successor.parent.left_child:
                successor.parent.left_child = successor.right_child
            else:
                successor.parent.right_child = successor.right_child

            if successor.right_child is not None:
                successor.right_child = successor.parent


    def print_sorted_tree(self):
        print_inorder(self.root)