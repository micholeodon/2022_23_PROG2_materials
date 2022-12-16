def sumFromNtoM(N,M):
    n1 = N
    n2 = M

    if N == M:
        return N

    if n2 < n1:
        n1, n2 = n2, n1

    suma = 0
    for n in range(n1, n2+1):
        suma += n
        
    return suma


print(sumFromNtoM(5,3))