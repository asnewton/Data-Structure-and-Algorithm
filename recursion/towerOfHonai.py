# Tower of Hanoi

def toh(source, destination, helper, n):
    if(n == 0):
        return

    toh(source, helper, destination, n-1)
    print("Move "+str(n) +"th disk from " + source + " to " + destination)
    toh(helper, destination, source, n-1)


if __name__ == "__main__":
    toh("A", "B", "C", 3)
