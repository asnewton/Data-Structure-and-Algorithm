# python program to sort an array using quicksort

# this fun returns pivot index
def partition(arr, low, high, pivot):
    itr = low
    parIdx = low
    while(itr <= high):
        if(arr[itr] <= pivot):
            arr[itr], arr[parIdx] = arr[parIdx], arr[itr]
            itr += 1
            parIdx += 1
        else:
            itr += 1
        
    return parIdx - 1

def quicksort(arr, low, high):
    if low >= high:
        return
    pivot = arr[high]
    pivIdx = partition(arr, low, high, pivot)
    quicksort(arr, low, pivIdx-1)
    quicksort(arr, pivIdx+1, high)

if __name__ == "__main__":
    a = [2, 5, 3, 9, 4, 15, 55, 19, 20]
    quicksort(a, 0, len(a)-1)
    print(a)