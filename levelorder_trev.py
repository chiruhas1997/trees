class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def printCurrentLevel(root,level):
    if root==None:
        return
    if level==1:
        print(root.info,end=' ')
    if level >1:
        printCurrentLevel(root.left,level-1)
        printCurrentLevel(root.right,level-1)

def getHeight(root):
    if root == None:
        return 1
    count = max(getHeight(root.left),getHeight(root.right))+1
    return count
        
def levelOrder(root):
    height = getHeight(root)
    for level in range(1,height+1):
        printCurrentLevel(root,level)
    #Write your code here



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)