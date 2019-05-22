# Python program to find maximum value of Sum(i*arr[i])
# returns max possible value of Sum(i*arr[i]) 

def maxSum(arr):
    arrSum = 0
    currVal = 0
    n = len(arr)

    for i in range(len(arr)):
        arrSum += arr[i]
        currVal += i * arr[i]

    maxVal = currVal

    for j in range(1,len(arr)):
        currVal += arrSum - (n * arr[n-j])
        if(currVal > maxVal):
            maxVal = currVal
        
    return(maxVal)

if __name__ == "__main__":
    arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
    print(maxSum(arr))