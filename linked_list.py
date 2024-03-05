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

    def prepend(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node

        self._length += 1

    def delete_first(self):
        if not self.head:
            return

        if self.head is self.tail:
            temp = self.head
            self.head = None
            self.head = None
            del temp

        else:
            temp = self.head
            self.head = self.head.next
            del temp
        
        self._length -= 1

    def delete_last(self):
        if not self.head:
            return
        
        if self.head is self.tail:
            temp = self.tail
            self.head = self.tail = None
            del temp

        else:
            before_last = self.head
            while before_last.next.next:
                before_last = before_last.next

            temp = self.tail
            self.tail = before_last
            self.tail.next = None
            del temp

        self._length -= 1

    def get_by_index(self, index:int)->Node:
        if not self.head:
            raise KeyError('Given index does not exist.')     
        
        if index >= self._length or index < -1:
            raise KeyError('Given index does not exist.')
        
        if self.head is self.tail:
            return self.head

        if index == -1:
            return self.tail
        
        node = self.head
        for _ in range(index):
            node = node.next

        return node
    
    def set(self, index:int, value)->bool:
        if not self.head:
            raise KeyError('Given index does not exist.')
        
        if index >= self._length or index < -1:
            raise KeyError('Given index does not exist.')
        
        if index == -1:
            self.tail.value = value
            return True
        
        if index == 0:
            self.head.value = value
            return True
        
        node = self.head
        for _ in range(index):
            node = node.next

        node.value = value
        return True

    def reverse(self):
        if not self.head:
            return
        
        if self._length == 1:
            return
        
        before = None
        current: Node = self.head
        next_node: Node = self.head.next
        while current:
            current.next = before
            before = current
            current = next_node
            next_node = next_node.next if next_node else None

        self.head, self.tail = self.tail, self.head

    def insert(self, index:int, value)->bool:
        if index >= self._length or index < 0:
            raise KeyError('Given index does not exist.')
        
        if index == 0:
            self.prepend(value)
            self._length += 1
            return True
        
        new_node = Node(value)
        before = self.head
        after = self.head.next
        for _ in range(index-1):
            before = before.next
            after = after.next

        before.next = new_node
        new_node.next = after
        self._length += 1
        return True
    
    def get_by_value(self, value)-> Node:

        """
        First occurrence of the value. Retrun node.
        """

        if not self.head:
            return None
        
        node = self.head 
        while node:
            if node.value == value:
                break
            node = node.next

        return node
    
    def remove(self, value)->bool:
        node_to_remove = self.get_by_value(value)
        if not node_to_remove:
            return False
        
        if self.head is node_to_remove:
            self.delete_first()
            return True
        
        if self.tail is node_to_remove:
            self.delete_last()
            return True


        temp_node = self.head.next
        before_node = self.head
        while temp_node:
            if temp_node is node_to_remove:
                break
            before_node = temp_node
            temp_node = temp_node.next

        next_node = temp_node.next
        before_node.next = next_node
        self._length -= 1
        del temp_node
        del node_to_remove
        return True


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

    
if __name__ == '__main__':

    ll = LinkedList(2)
    ll.append(3)
    ll.append(5)
    ll.append(8)
    ll.append(45)
    ll.append(23)
    ll.append(1)
    ll.prepend(66)
    ll.insert(2, 32)
    ll.delete_first()
    ll.delete_last()
    ll.set(-1, 48)
    print(ll.print_linked_list())
    ll.reverse()
    ll.remove(32)
    print(ll.print_linked_list())
    print(ll.length())
    print(ll.get_by_index(5).value)