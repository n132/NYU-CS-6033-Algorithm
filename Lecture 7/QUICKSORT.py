import random
def PARTITION(A,l,r):
    x = A[r-1]
    i = l-1
    for _ in range(l,r-1):
        if A[_]<x:
            i+=1
            tmp = A[_]
            A[_] = A[i]
            A[i] = tmp
    tmp = A[r-1]
    A[r-1] = A[i+1]
    A[i+1] = tmp
    return i+1
def RANDOM_PARTITION(A,l,r):
    x = random.randint(l,r-1)
    tmp = A[x]
    A[x] = A[r-1]
    A[r-1] = tmp
    return PARTITION(A,l,r)
def QUICKSORT(A,l,r):
    if l< r:
        # k = PARTITION(A,l,r)
        k = RANDOM_PARTITION(A,l,r)
        QUICKSORT(A,l,k)
        QUICKSORT(A,k+1,r)
if __name__ == "__main__":
    A = [_ for _ in range(-0x100,0x100)]
    for _ in range(0x100):
        random.shuffle(A)
        QUICKSORT(A,0,len(A))
        assert(A==[_ for _ in range(-0x100,0x100)])
    print("Done")