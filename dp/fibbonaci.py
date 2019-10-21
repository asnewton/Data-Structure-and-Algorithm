#fibbonacci using dynamic programming

def fibbo(n, qb):
    if(n==0 or n==1):
        return n
    if(qb[n] != 0):
        return qb[n]
    
    temp = fibbo(n-1, qb) + fibbo(n-2, qb)
    qb[n]=temp
    return temp
    
print(fibbo(9, [0]*10))
    