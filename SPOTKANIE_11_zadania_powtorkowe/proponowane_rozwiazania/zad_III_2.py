# ciag arytmetyczny

def arithmeticSequence(n, a0, r):

    an = a0 + n*r
    Sn = a0 

    for k in range(1, n+1):
        Sn += k*r

    return (an, Sn)

n = 3
a0 = 1
r = 4
print(arithmeticSequence(n,a0,r))