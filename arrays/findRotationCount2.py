# Find rotation count of array

def rotationCount(arr, start, end):
    if(start > end):
        return
    if(start == end):
        return(start)

    mid = int((start + end) / 2)

    if(start < mid and arr[mid] < arr[mid-1]):
        return(mid)
    if(mid < end and arr[mid] > arr[mid+1]):
        return(mid+1)

    if(arr[end] > arr[mid]):
        return(rotationCount(arr, mid+1, end))
    else:
        return(rotationCount(arr, start, mid-1))
    
if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12] 
    print(rotationCount(arr, 0, len(arr)-1))