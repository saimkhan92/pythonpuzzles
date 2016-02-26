# Prints the nodes of a binary tree "k" levels down the root

class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def node_at_k_distance(root,k):
    
    if root==None or k<0:
        return
    
    if k==0:
        print (root.data)
        return
    
    node_at_k_distance(root.left,k-1)
    node_at_k_distance(root.right, k-1)
    

root=Node(20)
root.left=Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
node_at_k_distance(root, 2)
