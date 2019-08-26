class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def kfarfromNode(node, k):
    if( k < 0 or node is None):
        return
    if(k == 0):
        print(node.data)
        return
    
    kfarfromNode(node.left, k-1)
    kfarfromNode(node.right, k-1)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    kfarfromNode(root, 2)