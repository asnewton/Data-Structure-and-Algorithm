# program for rearrange an array such that arr[i] = i. 

def rearrangeArray(arr):
    n = len(arr)
    s = set()

    for i in range(n):
        s.add(arr[i])
    for j in range(n):
        if( j in s):
            arr[j] = j
        else:
            arr[j] = -1

    return(arr)

if __name__ == "__main__":
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    print(rearrangeArray(arr))