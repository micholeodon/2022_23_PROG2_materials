def printFibonUpToN(N):

    lista = []

    if N == 0:
        print(0)
        lista.append(0)

    if N >= 1:
        print(0)
        print(1)
        print(1)
        lista.append(0)
        lista.append(1)
        lista.append(1)

    if N > 1:
        prev = 1
        next = 2

        while next <= N:            
            print(next)
            lista.append(next)
            tmp = next
            next = prev + next 
            prev = tmp
            
    return lista

odp = 0
while 1:
    odp = input('Podaj N: ')
    if odp.upper() == "END":
        break
    
    N = float(odp)
    
    L = printFibonUpToN(N)
    print(f"L: {L}")