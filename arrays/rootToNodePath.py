# Python program to  find the path of a given node from root in a binary tree

class BinaryP:
    def rootToNodePath(root, node):
        if(root.data == node.data):
            return([node.data])
        if(node is None):
            return([])

        isInLeftChild = rootToNodePath(root.left, node)
        if(len(isInLeftChild) > 0):
            return(isInLeftChild.append(root.data))
        
        isInRightChild = rootToNodePath(root.right, node)
        if(len(isInRightChild) > 0):
            return(isInRightChild.append(root.data))


        