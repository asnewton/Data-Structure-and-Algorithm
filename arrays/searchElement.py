# Python Program to search an element in a sorted and pivoted array 

def findPivot(arr, low, high):
    if(low > high):
        return(-1)

    if(low == high):
        return(low)

    mid = int((low + high) / 2)

    if(mid < high and arr[mid] > arr[mid+1]):
        return(mid)
    if(mid > low and arr[mid] < arr[mid-1]):
        return(mid-1)
    
    if(arr[low] >= arr[mid]):
        return(findPivot(arr, low, mid-1))
    else:
        return(findPivot(arr, mid+1, high))


def binarySearch(arr, low, high, elem):
    if(low > high):
        return(-1)
    
    if(low == high):
        return(low)
    
    mid = int((low + high) / 2)

    if(elem == arr[mid]):
        return(mid)
    if(elem > arr[mid]):
        return(binarySearch(arr, mid+1, high, elem))
    else:
        return(binarySearch(arr, low, mid-1, elem))



def searchElement(arr, elem):
    n = len(arr)
    pivot = findPivot(arr, 0, n-1)

    if(elem == arr[pivot]):
        return(pivot)

    if(elem >= arr[0]):
        return(binarySearch(arr, 0, pivot-1, elem))
    else:
        return(binarySearch(arr, pivot+1, n-1, elem))
        


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    print(searchElement(arr, 2))