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

# aMax = 0
# bMax = 0
# nMax = 0
# primes = ESieve(87400)
# for a in range(-1000, 1000):
#     for b in range(-1000, 1000):
#         n = 0
#         print('n is', n, 'a is', a, 'b is', b)
#         while isPrime(abs(n*n + a*n +b)):
#             n = n + 1
#             print('n in while', n)
#         if n > nMax:
#             aMax = a
#             bMax = b
#             nMax = n
# print(nMax, aMax, bMax, aMax*bMax)

# Shrinking solution space
# If n = 0, b must be prime
# Since all primes except 2 are odd, so if b=2, a has to be even

# This runs MUCH faster...
aMax = 0
bMax = 0
nMax = 0
primes = ESieve(87400)
bPos = ESieve(1000) # we have cut down the solution space substantially
for a in range(-999, 1001, 2):
    for i in range(1, len(bPos)):
        for j in range(2):
            n = 0
            sign = (j==0) if 1 else -1
            aOdd = (i%2==0) if -1 else 0 #Making a even if b is even
            while isPrime(abs(n*n + (a+aOdd)*n +sign*bPos[i])):
                n = n + 1
            if n > nMax:
                aMax = a
                bMax = bPos[i]
                nMax = n
                print(nMax, aMax, bMax)
print(nMax, aMax, bMax, aMax*bMax)
