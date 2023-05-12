def pickNumbers(A):
    if len(A)<=2:
        return min(A)
    return min([A[0]+sum(A[1:])-pickNumbers(A[1:]),A[-1]+sum(A[:-1])-pickNumbers(A[:-1])])
print(pickNumbers([100,3,100,3]))