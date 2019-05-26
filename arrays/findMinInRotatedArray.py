# Python program to find minimum element in  rotated and sorted array

def findMin(arr):
    n = len(arr)

    for i in range(1, n):
        if(arr[i-1] > arr[i]):
            print(arr[i])

        
if __name__ == "__main__":
    arr = [ 3, 4, 5, 6, 7, 8,1, 2] 
    findMin(arr)