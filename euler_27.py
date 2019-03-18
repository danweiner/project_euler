from euler_21 import ESieve

# Assumes list of ordered primes larger than test num
def isPrime(testNumber):
    i = 0
    while primes[i] <= testNumber:
        if primes[i] == testNumber:
            return True
        i = i + 1
    return False


# Use Brute Force to test all possibilities
# Takes a LONG time to run...

aMax = 0
bMax = 0
nMax = 0
primes = ESieve(87400)
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 0
        print('n is', n, 'a is', a, 'b is', b)
        while isPrime(abs(n*n + a*n +b)):
            n = n + 1
            print('n in while', n)
        if n > nMax:
            aMax = a
            bMax = b
            nMax = n
print(nMax, aMax, bMax, aMax*bMax)
