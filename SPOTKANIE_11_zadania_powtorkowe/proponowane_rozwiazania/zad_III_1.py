# liczby pierwsze funkcja

# The prime numbers from 1 to 100 are: 
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
# 73, 79, 83, 89, 97.

def isPrime(n):
    
    for k in range(2, n):
        if n % k == 0: 
            return False
        
    return True

    
for n in range(1, 100):

    #print(f"{n} : {isPrime(n)}")

    if isPrime(n):
        print(n, end=', ')