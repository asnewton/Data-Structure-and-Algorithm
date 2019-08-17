# Pytho program to perform deletion in a Binary Tree and replacing the deleted valcancy from the rightmost child of the right child


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if(root is None):
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def deleteRightmost(root, node):
    if root is None:
        return
    
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp == node:
            temp = None
        if temp.left:
            if temp.left == node:
                temp.left = None
                break
            else:
                q.append(temp.left)
        if temp.right:
            if temp.right == node:
                temp.right = None
                break
            else:
                q.append(temp.right)
            

def deletion(root, key):
    if(root is None):
        return

    if(root.right is None and root.left is None):
        if (root.data == key):
            return

    temp = root
    while(temp.right):
        temp = temp.right

    q = []
    q.append(root)
    while(len(q) > 0):
        root = q.pop(0)
        if root.data == key:
            root.data = temp.data
            break
        elif root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

    deleteRightmost(root, temp)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    inorder(root)
    deletion(root, 10)
    print("\n")
    inorder(root)
