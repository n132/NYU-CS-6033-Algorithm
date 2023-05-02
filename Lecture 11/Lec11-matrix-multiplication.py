input_matrix  =  [30,1,40,10,25]
def matrix_chain_multiplication(A):
    n  = len(A)-1
    T = [[0 for __ in range(n+1)] for _ in range(n+1)]
    for off in range(1,n):
        for start in range(n,0,-1):
            end = start + off
            if end>n:
                continue
            T[start][end] = min([T[start][t]+T[t+1][end]+A[start-1]*A[t]*A[end] for t in range(start,end)])
    return T[1][n]
print(matrix_chain_multiplication(input_matrix))
