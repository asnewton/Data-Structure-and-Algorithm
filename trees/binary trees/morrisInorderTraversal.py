# Python program to do inorder traversal using morris traversal  

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def morrisInorder(root):
    if root is None:
        return

    curr = root
    while(curr):
        if curr.left is None:
            print(curr.data)
            curr = curr.right
        else:            
            pred = curr.left
            while(pred.right is not None and pred.right != curr):
                pred = pred.right
            if pred.right is None:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                print(curr.data)
                curr = curr.right



if __name__ == "__main__":
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    morrisInorder(root)