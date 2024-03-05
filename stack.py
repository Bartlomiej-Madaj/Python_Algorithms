from linked_list import Node

class Stack:
    def __init__(self, value=None):
        self.top = None
        self._length = 0

        if value:
            self.push(value)

        
    def push(self, value):
        new_node = Node(value)

        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self._length += 1

    def pop(self)->Node:

        if not self.top:
            return None
        
        temp = self.top
        if self._length == 1:
            self.top = None
        else:
            self.top = self.top.next

        return temp
    
    def print(self):
        if not self.top:
            print('[]')

        else:
            str_stack = '[ '
            temp = self.top
            while temp:
                str_stack += f'{temp.value}, '
                temp = temp.next

            str_stack += f']'

            print(str_stack)

        
    

if __name__ == '__main__':

    st = Stack(5)
    st.push(7)
    st.push(10)
    st.print()
    st.pop()
    st.print()