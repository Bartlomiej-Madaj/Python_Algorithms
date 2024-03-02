from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.value}"


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._pre_dfs_values = list()

    def insert(self, value:int)->bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def BFS(self)->list:
        searched_values = list()
        if not self.root:
            return searched_values
        
        search_deque = deque()
        search_deque.append(self.root)
        
        while search_deque:
            node = search_deque.popleft()
            searched_values.append(node.value)
            if node.left:
                search_deque.append(node.left)
            if node.right:
                search_deque.append(node.right)

        return searched_values
    
    def pre_DFS(self, node=None)->list:
        # searched_values = list()
        if not self.root:
            return
        
        if node is None:
            node = self.root

        self._pre_dfs_values.append(node.value)

        if node.left:
            self.pre_DFS(node.left)
        if node.right:
            self.pre_DFS(node.right)

        
        # search_deque = deque()
        # search_deque.append(self.root)
        # current_node = search_deque[-1]
        # while search_deque:
        #     print(current_node)
        #     if  current_node.left and not current_node.value in searched_values:
        #         search_deque.append(current_node.left)
        #         searched_values.append(current_node.value)
        #         current_node = search_deque[-1]
        #     elif current_node.right and not current_node.right.value in searched_values:
        #         search_deque.append(current_node.right)
        #         searched_values.append(current_node.value)
        #         current_node = search_deque[-1]
        #     else:
        #         search_deque.pop()
        #         if search_deque:
        #             current_node = search_deque[-1]

        # return searched_values

               


bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(18)
bst.insert(27)
bst.insert(76)
bst.insert(52)
bst.insert(82)

print(bst.BFS())
print(bst.pre_DFS())
print(bst._pre_dfs_values)


