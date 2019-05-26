# Python program to find minimum element in  rotated and sorted array

def findMin(arr, start, end):
    if(end < start):
        return(arr[0])

    if(start > end):
        return

    if(start == end):
        return(arr[start])

    mid = int((start + end) / 2)

    if(mid > start and arr[mid] < arr[mid-1]):
        return(arr[mid])

    if(mid < end and arr[mid] > arr[mid+1]):
        return(arr[mid+1])

    if(arr[end] > arr[mid]):
        return(findMin(arr, start, mid-1))
    else:
        return(findMin(arr, mid+1, end))

    
if __name__ == "__main__":
    arr = [ 3, 4, 5, 6, 7, 8,1, 2] 
    print(findMin(arr, 0, len(arr)-1))