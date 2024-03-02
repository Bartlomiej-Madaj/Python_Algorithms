class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self._length = 0
        if value:
            self.append(value)

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._length += 1

    def print_linked_list(self):
        str_linked = ''
        if not self.head:
            return str_linked
        node = self.head

        while node:
            str_linked += f'{node.value} '
            node = node.next

        return str_linked
    
    def length(self):
        return self._length

    


ll = LinkedList(2)
ll.append(3)
ll.append(5)
ll.append(8)
ll.append(45)
ll.append(23)
ll.append(1)

print(ll.print_linked_list())
print(ll.length())