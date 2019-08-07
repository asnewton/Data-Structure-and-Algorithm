# Python program to shift all zeros at the end

def zeroAtEnd(arr):
    count = 0
    for i in range(len(arr)):
        if(arr[i] != 0):
            arr[count] = arr[i]
            count += 1

    while(count < len(arr)):
        arr[count] = 0
        count += 1

    if __name__ == "__main__":
        arr = [1, 2, 3, 0, 4, 0, 5, 0, 7, 8]
        zeroAtEnd(arr)
        print(arr)
    