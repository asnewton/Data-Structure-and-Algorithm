# inorder traversal without recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    
    stack = []
    curr = root
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif(stack):
            curr = stack.pop()
            print(curr.data, end=" ")
            curr = curr.right
        else:
            break


if __name__ == "__main__":
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5)
    inorder(root)
