# Find rotation count of array

def rotationCount(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if(min > arr[i]):
            min = arr[i]
            return(i)
    

if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12] 
    print(rotationCount(arr))