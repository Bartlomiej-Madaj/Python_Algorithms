from typing import List, Set

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f'{self.key}: {self.value}'
    
    def __repr__(self) -> str:
        return f'Node({self.key}, {self.value})'

class HashTable:
    _size = 7
    def __init__(self):
        self._table:List[Node] = [None for _ in range(HashTable._size)]

    def set(self, key:str, value):
        index = self._hash(key)
        new_node = Node(key, value)
        if self._table[index] is None:
            self._table[index] = new_node

        else:
            node = self._table[index]
            while node:
                if node.key == key:
                    node.value = value
                    return
                node = node.next

            new_node.next = self._table[index]
            self._table[index] = new_node

    def get(self, key):
        index = self._hash(key)

        if self._table[index] is None:
            raise KeyError('Given key does not exist.')
        
        node: Node = self._table[index]
        while node:
            if node.key == key:
                return node.value
            
            node = node.next

        raise KeyError('Given key does not exist.')
    
    def keys(self)->Set[str]:
        """
        Return a set of keys.
        """
        _keys = set()
        for i in self._table:
            node: Node = i
            while node:
                _keys.add(node.key)
                node = node.next

        return _keys

    def _hash(self, key:str) -> int:
        if not isinstance(key, str):
            raise ValueError('The key has to be string type.')
        hash_value = 0
        for i in key:
            hash_value += ord(i)

        return hash_value % HashTable._size
    
    def print(self):
        if all(x is None for x in self._table):
            return '{}'

        printed_str = '{ \n'
        for i in self._table:
            if i is None:
                continue
            node:Node = i
            while node:
                printed_str += f'  {node.key}: {node.value}, \n'
                node = node.next

        printed_str += '}'
    
        return printed_str
    

ht = HashTable()
ht.set('apple', 3)
print(ht._table)
ht.set('banana', 5)
print(ht.print())
ht.set('apple', 1)
print(ht.print())
print(ht.keys())