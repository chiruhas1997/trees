

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        seld.right=None

class BinaryTree:
    def create_node(self,data):
        return Node(data)

    def insert(self,node,data):
        
        if node == None:
            node = Node(data)
            return node
        if data<node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
