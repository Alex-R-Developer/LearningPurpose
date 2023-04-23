from hash_table_chaining import LinkedList

class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [LinkedList() for _ in range(self._capacity)]

    def _hash_function(self, key):
        return hash(key) % self._capacity


    def _get_linked_list_for_key(self, key):
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]


    def _look_up_node(self, key):
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        return self._look_up_node(key).value

            
    def insert(self, key, value):
        existing_node = self._look_up_node(key)

        if existing_node is not None:
            existing_node.value = value
        else:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)

    def delete_by_key(self, key):
        node_to_delete = self._look_up_node(key)

        if node_to_delete is not None:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.delete(node_to_delete)
            
    def __str__(self):
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]