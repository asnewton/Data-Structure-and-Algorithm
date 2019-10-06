# Construct Ancestor Matrix from a Given Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1
    
def createAncestorMatrix(root, ancArr, ancMat):
    if root is None:
        return
    
    for item in ancArr:
        ancMat[item.data][root.data] = 1

    ancArr.append(root)
    createAncestorMatrix(root.left, ancArr, ancMat)
    createAncestorMatrix(root.right, ancArr, ancMat)
    ancArr.remove(root)

def ancMatUtil(root):
    n = size(root)
    ancMat = [[0 for x in range(n)] for y in range(n)]
    ancArr = []
    createAncestorMatrix(root, ancArr, ancMat)
    return ancMat


if __name__ == "__main__":
    root = Node(5)  
    root.left = Node(1)  
    root.right = Node(2)  
    root.left.left = Node(0)  
    root.left.right = Node(4)  
    root.right.left = Node(3)
    m = ancMatUtil(root)
    print(m)
