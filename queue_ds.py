from linked_list import Node

class Queue:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self._length = 0
        if value:
            self.enqueue(value)

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._length += 1

    def dequeue(self):
        if not self.head:
            return
        
        dequeued_node = self.head

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        self._length -= 1

        return dequeued_node
    
    def print_queue(self):
        if not self.head:
            print('[]')
        str_queue = '[ '

        temp = self.head
        while temp:
            str_queue += f'{temp.value}, '
            temp = temp.next

        str_queue += ']'
        print(str_queue)

    def __iadd__(self, other:'Queue'):
        if not isinstance(other, Queue):
            raise TypeError('Item has to be Queue instance.')
        
        temp = other.head
        while temp:
            self.enqueue(temp.value)
            temp = temp.next

        return self
    
    def __add__(self, other:'Queue'):
        if not isinstance(other, Queue):
            raise TypeError('Item has to be Queue instance.')
        new_queue = Queue()
        if self.head:
            temp = self.head
            while temp:
                new_queue.enqueue(temp.value)
                temp = temp.next
        if other.head:
            other_temp = other.head
            while other_temp:
                new_queue.enqueue(other_temp.value)
                other_temp = other_temp.next

        return new_queue
    


    def __len__(self):
        return self._length
    
    def __str__(self):
        return str(self.__class__)
    
    def __repr__(self):
        return f"Queue(value)"
    
if __name__ == '__main__':
    qu = Queue(4)
    qu2 = Queue(7)

    qu.print_queue()

    qu.enqueue(5)

    qu.print_queue()

    qu += qu2

    qu.print_queue()

    qu3 = qu + qu2

    qu3.print_queue()

    print(qu)

    print(len(qu))


