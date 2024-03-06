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

class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1

class AVLTree:

    def __init__(self, value):
        self.root = AVLNode(value)

    def search(self, value):
        temp:AVLNode = self.root

        while not temp is None and temp.value != value:
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return temp
    
    def insert(self, root: AVLNode, value) -> AVLNode:
        if not root:
            return AVLNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), 
                              self.get_height(root.right))

        bf = self.get_balance_factor(root)

        if bf > 1 and value < root.left.value:
            return self._right_rotate(root)
        
        if bf < -1 and value > root.right.value:
            return self._left_rotate(root)
        
        if bf > 1 and value > root.left.value:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        
        if bf < -1 and value < root.right.value:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root
    
    def delete(self, root:AVLNode, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            temp = self.get_min_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Update the balance factor and balance the tree
        bf = self.get_balance_factor(root)

        if bf > 1 and self.get_balance_factor(root.left) >= 0:
            return self._right_rotate(root)
        
        if bf < -1 and self.get_balance_factor(root.right) <= 0:
            return self._left_rotate(root)
        
        if bf > 1 and self.get_balance_factor(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        
        if bf < -1 and self.get_balance_factor(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root
    
    def print_tree(self):
        if self.root:
            queue = deque()
            queue.append(self.root)

            level_order = ''
            level_order_with_details = ''

            while(queue):
                node = queue.popleft()
                level_order += f'{node.value} '
                level_order_with_details += f'{node.value}: '.ljust(5) + f'h = {self.get_height(node)}, bf = {self.get_balance_factor(node)}\n'

                # add children to queue
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            print('\nLevel-order traversal:')
            print(level_order)
            print(f'\nLevel-order traversal with height and balance factor:') 
            print(level_order_with_details)
        else:
            print('\nAVL tree is empty!')

    def get_balance_factor(self, node:AVLNode):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        return left_height - right_height
    

    def _left_rotate(self, node:AVLNode)->AVLNode:
        B: AVLNode = node.left
        Y = B.left

        B.left = node
        node.right = Y

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        B.height = 1 + max(self.get_height(B.left),
                           self.get_height(B.right))
        
        return B
    
    def _right_rotate(self, node:AVLNode)->AVLNode:
        A:AVLNode = node.left
        Y = A.right

        A.right = node
        node.left = Y

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        A.height = 1 + max(self.get_height(A.left),
                           self.get_height(A.right))
        
        return A

    def get_height(self, node:AVLNode)->int:
        return node.height if node else 0
    
    def get_min_node(self, node):
        return node if not node or not node.left else self.get_min_node(node.left)


bst = BinarySearchTree()
# bst.insert(47)
# bst.insert(21)
# bst.insert(18)
# bst.insert(27)
# bst.insert(76)
# bst.insert(52)
# bst.insert(82)

# print(bst.BFS())
# print(bst.pre_DFS())
# print(bst._pre_dfs_values)

avl = AVLTree(4)

avl.insert(avl.root, 5)

avl.delete(avl.root, 4)
avl.print_tree()
# avl.insert(43)


