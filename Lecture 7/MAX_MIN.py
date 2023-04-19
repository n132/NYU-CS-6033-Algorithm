import math
import random
def max(A):
    res = -math.inf
    for x in A:
        if x > res:
            res=x
    return res
def min(A):
    res = math.inf
    for x in A:
        if x < res:
            res=x
    return res
def MAX_MIN(A):
    # n/2 * 3 = 1/5n
    W = []
    L = []
    for _ in range(0,len(A),2):
        if _+1>= len(A):
            W.append(A[_])
            L.append(A[_])
            break

        if A[_] > A[_+1]:
            W.append(A[_])
            L.append(A[_+1])
        else:
            W.append(A[_+1])
            L.append(A[_])
    mmm = max(W)
    lll = min(L)
    return mmm,lll
if __name__ == "__main__":
    A = [_ for _ in range(0x100)]
    for _ in range(0x100):
        random.shuffle(A)
        a,b = MAX_MIN(A)
        assert(a==max(A))
        assert(b==min(A))
    print("Done")