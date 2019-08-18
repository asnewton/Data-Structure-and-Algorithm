# python program to make expression tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def isOp(char):
    if char == '+' or char == '-' or char == '/' or char == '*':
        return True
    return False

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def expressionTree(postfix):
    stack = []
    for i in postfix:
        if not isOp(i):
            node = Node(i)
            stack.append(i)
        else:
            node = Node(i)
            r = stack.pop()
            l = stack.pop()
            node.left = l
            node.right = r
            stack.append(node)
    item = stack.pop()
    return item   

if __name__ == "__main__":
    postfix = "ab+ef*g*-"
    tree = expressionTree(postfix)
    inorder(tree)