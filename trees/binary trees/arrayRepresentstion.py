# array implementation of tree

arr = [None] * 10

def insertRoot(root):
    arr[0] = root

def insertLeft(node, pos):
    p = 2 * pos + 1
    if arr[pos] is not None: # parent is present
        arr[p] = node

        

def insertRight(node, pos):
    p = 2 * pos + 2
    if arr[pos] is not None: # parent is present
        arr[p] = node

if __name__ == "__main__":
    insertRoot("A")
    insertLeft("B", 0)
    insertRight("C", 0)
    insertLeft("D", 1)
    insertRight("E", 1)
    insertLeft("F", 2)
    print(arr)