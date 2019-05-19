# Python Program to search an element in a sorted and pivoted array 

def searchElement(arr,low, high, elem):
    if(low > high):
        return(-1)

    mid = int((low + high) / 2)

    if(elem == arr[mid]):
        return(mid)

    if(arr[low] <= arr[mid]):
        if(elem >= arr[low] and elem <= arr[mid]):
            return(searchElement(arr, low, mid-1, elem))
        else:
            return(searchElement(arr, mid+1, high, elem))
    
    if(elem >= arr[mid] and elem <= arr[high]):
        return(searchElement(arr, mid+1, high, elem))
    else:
        return(searchElement(arr,low, mid-1,  elem))
    

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
    print(searchElement(arr, 0, len(arr)-1, 2))     