# Rearrange positive and negative numbers in O(n) time and O(1) extra space

def rearrangArray(arr):
    n = len(arr)
    i = -1
    for j in range(n):
        if(arr[j] < 0):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    neg = 0
    pos = i+1    
    while(neg < pos and pos < n and arr[neg] < 0):
        print(arr)
        arr[pos], arr[neg] = arr[neg], arr[pos]
        pos += 1
        neg += 2
    print(arr)

if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    rearrangArray(arr)