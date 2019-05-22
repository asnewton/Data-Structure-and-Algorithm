# Maximum sum of i*arr[i] among all rotations of a given array

def maxSum(arr):
    n = len(arr)

    currSumOfElem = 0
    for i in range(n):
        currSumOfElem += arr[i]
    
    currSumOfIndexAndElem = 0
    for j in range(n):
        currSumOfIndexAndElem += j * arr[j]

    maxSumResult = currSumOfIndexAndElem
    for k in range(1, n):
        currSumOfIndexAndElem = currSumOfIndexAndElem - (currSumOfElem - arr[k-1]) + arr[k-1] * (n-1)
        if(maxSumResult < currSumOfIndexAndElem):
            maxSumResult = currSumOfIndexAndElem
        
    return(maxSumResult)

if __name__ == "__main__":
    arr = [8, 3, 1, 2]  
    print(maxSum(arr))
