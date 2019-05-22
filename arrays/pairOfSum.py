def isPairOfSum(arr, num):
    for i in range(len(arr)):
        temp = arr[i]
        for j in range(len(arr)):
            if(temp + arr[j] == num):
                return((temp, arr[j]), True)

    return(False)


if __name__ == "__main__":
    arr = [11, 15, 6, 8, 9, 10]
    print(isPairOfSum(arr, 14))