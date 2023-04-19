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
def ith_item(A,i):
    k = -1
    i = i-1
    while True:
        k = RANDOM_PARTITION(A,0,len(A))
        if k > i:
            RANDOM_PARTITION(A[:k],0,k)
        elif k< i:
            RANDOM_PARTITION(A[k+1:],0,len(A)-k-1)
        else:
            return A[k]
def RANDMIZED_SELECT(A,l,r,i):
    q = RANDOM_PARTITION(A,l,r)
    k = q-l+1
    if k==i:
        return A[q]
    elif k>i:
        return RANDMIZED_SELECT(A,l,q,i)
    else:
        return RANDMIZED_SELECT(A,q+1,r,i-k)
if __name__ == "__main__":
    A = [_ for _ in range(-0x100,0x100)]
    for _ in range(0x100):
        random.shuffle(A)
        x = random.randint(1,len(A)-1)
        res1 = ith_item(A,x)
        res2 = RANDMIZED_SELECT(A,0,len(A),x)    
        
        intended = [_ for _ in range(-0x100,0x100)][x-1]
        assert(res1 == intended)
        assert(res2 == intended)
    print("Done")
