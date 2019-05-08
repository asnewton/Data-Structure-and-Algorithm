# Python program to rotate an array by d elements 

def rotateArray(arr, d, n):
    for i in range(d):
        temp = arr[0]
        for j in range(1,n):
            arr[j-1] = arr[j]
        arr[n-1] = temp
        
    
if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)    
    rotateArray(arr, 2, n)
    print(arr)