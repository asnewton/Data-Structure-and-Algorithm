# Program for right rotation of  an array (Reversal Algorithm) 

def revreseArray(arr, start, end):
    if(start > end):
        return
    
    if(start == end):
        return(arr[start])

    while(start <= end):
        arr[start] , arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    

def rightRotate(arr, k):
    n = len(arr)
    revreseArray(arr, n-k, n-1)
    for i in range(k):
        temp = arr[n-1]
        for j in range(n-1, 0, -1):
            arr[j] = arr[j-1]
        arr[0] = temp
    return(arr)

if __name__ == "__main__":
    arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    revreseArray(arr, 7, 9)
    # print(arr)
    print(rightRotate(arr, 3))
    