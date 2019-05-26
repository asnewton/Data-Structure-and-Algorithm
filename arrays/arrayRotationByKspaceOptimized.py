# Python program to print array by k roatation

def arrayRotation(arr, k):
    n = len(arr)

    for i in range(k, n+k):
        print(arr[i%n], end=" ")

    
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    arrayRotation(arr, 2)
    