# Python program to find the k far down node in a binary tree

def kFarDown(node, k):
    if(node is None or k < 0):
        return
    
    if(k == 0):
        print(node.data)

    kFarDown(node.left, k-1)
    kFarDown(node.right, k-1)