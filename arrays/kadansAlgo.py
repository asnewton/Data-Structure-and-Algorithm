# Find sum of maximum subarray

def kadansAlgo(arr):
    localMax = arr[0]
    globalMax = arr[0]

    for i in range(1, len(arr)):
        localMax  = localMax + arr[i]
        if(localMax < arr[i]):
            localMax = arr[i]
        if(globalMax < localMax):
            globalMax = localMax
        
    return(globalMax)


if __name__ == "__main__":
    arr = [4, -3, -2, 2, 3, 1, -2, -3, 4, 2, -6, -3, -1, 3, 1, 2]
    print(kadansAlgo(arr))