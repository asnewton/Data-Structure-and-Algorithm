# program to find nth fibbonacci using dynamic programming tabulation technnique

def fibbonacci(n):
    tb = [0]*(n+1)
    tb[0] = 0
    tb[1] = 1
    if(n<=2):
        return n
    for i in range(len(tb)):
        if tb[i] == 0:
            tb[i] = tb[i-1]+tb[i-2]
    return tb[n]

print(fibbonacci(9))