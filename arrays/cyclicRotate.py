# Program to cyclic rotate an array

def cyclicRotate(arr):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    cyclicRotate(arr)
    print(arr)