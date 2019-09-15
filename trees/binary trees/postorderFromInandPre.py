# Print Postorder traversal from given Inorder and Preorder traversals

def postorder(inorder, preorder, n):
    root = preorder[0]
    if root in inorder:
        idx = inorder.index(root)

    if idx != 0:
        postorder(inorder[:idx], preorder[idx+1 :], len(inorder[:idx]))
    
    if idx != n-1:
        postorder(inorder[idx+1:], preorder[idx+1 :], len(inorder[idx+1]))

    print(inorder[idx])

if __name__ == "__main__":
    inorder = [4, 2, 5, 1, 3, 6]; 
    preorder = [1, 2, 4, 5, 3, 6]; 
    n = len(inorder) 
    postorder(inorder, preorder, n) 