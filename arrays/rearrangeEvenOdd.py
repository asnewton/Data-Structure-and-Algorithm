# Program to rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i


def rearrangeArray(arr):
    n = len(arr)
    temp = [None] * n

    for i in range(n):
        temp[i] = arr[i]

    temp.sort()

    even = int(n/2)
    odd = n-even
    j = odd-1
    for i in range(0, n, 2):
        arr[i] = temp[j]
        j -= 1
    
    j = odd
    for i in range(1, n, 2):
        arr[i] = temp[j]
        j += 1

    return(arr)

if __name__ == "__main__":
    arr = [ 1, 2, 3, 4, 5, 6, 7 ]
    print(rearrangeArray(arr))