def pairOfSum(arr, num):
    low = 0
    high = len(arr)-1
    count = 0
    arr.sort()
    while(low < high):
        if(arr[low] + arr[high] > num):
            high -= 1
        elif(arr[low] + arr[high] < num):
            low += 1
        else:
            count += 1
            low += 1
    return(count)

if __name__ == "__main__":
    arr = [11, 15, 6, 7, 9, 10]
    print(pairOfSum(arr, 16))