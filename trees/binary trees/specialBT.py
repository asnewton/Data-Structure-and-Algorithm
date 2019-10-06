# Construct Special Binary Tree from given Inorder traversal

class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def buildTree (inorder, start, end): 
	if start > end: 
		return None

	i = Max (inorder, start, end) 
	root = newNode(inorder[i]) 
	if start == end: 
		return root 
	root.left = buildTree (inorder, start, i - 1) 
	root.right = buildTree (inorder, i + 1, end) 

	return root 

def Max(arr, strt, end): 
	i, Max = 0, arr[strt] 
	maxind = strt 
	for i in range(strt + 1, end + 1): 
		if arr[i] > Max: 
			Max = arr[i] 
			maxind = i 
	return maxind 

def printInorder (node): 
	if node == None: 
		return
	printInorder (node.left) 
	print(node.data, end = " ") 
	printInorder (node.right) 

if __name__ == '__main__': 	
	inorder = [5, 10, 40, 30, 28] 
	Len = len(inorder) 
	root = buildTree(inorder, 0, Len - 1) 
	printInorder(root) 
