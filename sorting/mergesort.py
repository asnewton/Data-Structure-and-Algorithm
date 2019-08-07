# Python program to implement merge sort
# merge function takes two sorted arrays


def merge(a, b):
    n = len(a)
    m = len(b)
    i, j, k = 0, 0, 0
    result = []
    while(i < n and j < m):
        if(a[i] < b[j]):
            result.append(a[i])
            i += 1

        else:
            result.append(b[j])
            j += 1

    while(i < n):
        result.append(a[i])
        i += 1

    while(j < m):
        result.append(b[j])
        j += 1

    return result


def mergesort(arr, low, high):
    if(low == high):
        return arr[low]

    mid = (low + high) / 2
    first_half = mergesort(arr, low, mid)
    second_half = mergesort(arr, mid+1, high)
    merge(first_half, second_half)


if __name__ == "__main__":
    a = [2, 5, 3, 9, 4, 15, 55, 19, 20]
    mergesort(a, 0, len(a))

    print(a)
