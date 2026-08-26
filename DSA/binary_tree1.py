class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(5)
root.left=Node(3)
root.right=Node(1)
root.left.right=Node(6)

#Full binary tree has either 0 or 2 children
#Perfect binary tree is full binary tree with all leaf nodes at same level
#Complete binary tree means there should be no gap in level by level traversal
#Degenerate binary tree has only 0 or 1 children
#Skewed is directional degenerate binary tree
#Balanced binary tree means left subtree height minus right should be less than equal to 1

#Pre, post, in and level order traversal 

