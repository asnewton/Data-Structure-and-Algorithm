# Python program for level order insertion in binary tree


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data




def inorder(root):
    if(root is None):
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def insertion(temp, data):
    q = []
    q.append(temp)
    while(len(q) > 0):
        temp = q[0]
        q.pop(0)
        if(temp.left is None):
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)
        if(temp.right is None):
            temp.right = Node(data)
            break
        else:
            q.append(temp.right)
            

if __name__ == '__main__': 
    root = Node(10)  
    root.left = Node(11)  
    root.left.left = Node(7)  
    root.right = Node(9)  
    root.right.left = Node(15)  
    root.right.right = Node(8)  
    
    print("Inorder traversal before insertion:", end = " ") 
    inorder(root)  
    
    key = 12
    insertion(root, key)  
    
    print()  
    print("Inorder traversal after insertion:", end = " ") 
    inorder(root) 