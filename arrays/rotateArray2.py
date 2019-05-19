# Python program to rotate an array by d elements 

def rotateArray(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6 ,7, 8]
    n = len(arr)
    rotateArray(arr, 0, 1)
    rotateArray(arr, 2, n-1)
    rotateArray(arr, 0, n-1)
    print(arr)