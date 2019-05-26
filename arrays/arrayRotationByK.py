# Python program to print array by k roatation

def roatateArray(arr, k):
    n = len(arr)

    # copy arr in temp twice
    temp = [None] *  2 * n
    for i in range(n):
        temp[i] = temp[i+n] = arr[i]

    start = k % n
    for j in range(start, start+n):
        print(temp[j], end=" ")
    

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    roatateArray(arr, 2)
    