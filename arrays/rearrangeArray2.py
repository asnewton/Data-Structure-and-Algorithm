# program for rearrange an array such that arr[i] = i. 

def rearrangeArray(arr):
    n = len(arr)
    i = 0
    while(i < n):
        if(arr[i] >= 0 and arr[i] != i):
            arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
        else:
            i += 1
        
        
    return(arr)


        
if __name__ == "__main__":
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    print(rearrangeArray(arr))