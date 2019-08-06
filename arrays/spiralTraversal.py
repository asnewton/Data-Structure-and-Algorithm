arr = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

def spiralTraversal(arr):
    n = len(arr)
    m = len(arr[0])
    T = 0
    B = n-1
    L = 0
    R = m-1
    direction = 1
    while( T <= B and L <= R):
        if(direction == 1):
            for i in range(L, R):
                print(arr[T][i])
            T += 1
            direction = 2
        elif( direction == 2):
            for i in range(T, B):
                print(arr[i][R])
            R -= 1
            direction = 3
        elif(direction == 3):
            for i in range(R, L, -1):
                print(arr[B][i])
            L -= 1
            direction = 4
        elif(direction == 4):
            for i in range(B, T, -1):
                print(arr[i][L])
            L += 1
            direction = 1
        direction = (direction + 1) % 5
spiralTraversal(arr)