import math
from bitstring import BitArray

# def sumUpDivisors(n):
#     total = 0
#     for i in range(1, n//2+1):
#         if n % i == 0:
#             total += i
#     return total
#
# def amicableNumbers(L):
#     total = 0
#     for i in L:
#         sumOfDivisors = sumUpDivisors(i)
#         if sumOfDivisors > i:
#             otherSum = sumUpDivisors(sumOfDivisors)
#             if otherSum == i:
#                 print('i is equal to', i, 'otherSum', otherSum)
#                 total += i
#                 total += sumOfDivisors
#     return total
#
# L = list(range(2, 10000))
# print(amicableNumbers(L))

# Solve using prime factorization
def sumOfFactorsPrime(num, primeList):
    n = num
    sum = 1
    p = primeList[0]
    i = 0
    while p*p <= n and n > 1 and i < len(primeList):
        p = primeList[i]
        i = i + 1
        if n%p == 0:
            j = p*p
            n = n/p
            while n%p == 0:
                j = j*p
                n = n/p
            sum = sum * (j-1)/(p-1)
    # A prime factor larger than sqrt remains, so add that
    if n>1:
        sum *= n+1

    return sum - num

def ESieve(upperLimit):
    # create a BitArray with upperLimit zero bits
    # the bits will be set to indicate that the bit position isnt prime
    has_factors = BitArray(upperLimit)
    prime_factors = []
    for i in range(2, upperLimit):
        if not has_factors[i]:
            prime_factors.append(i)
            # set all multiples of our prime to 1
            has_factors.set(True, range(i*2, upperLimit, i))
    return prime_factors


# sumAmicable = 0
# upperLimit = 10000
# primeList = ESieve(int(math.sqrt(upperLimit)+1))
#
# for i in range(2, upperLimit+1):
#     factorsi = sumOfFactorsPrime(i, primeList)
#     if factorsi > i and factorsi <= upperLimit:
#         factorsj = sumOfFactorsPrime(factorsi, primeList)
#         if factorsj == i:
#             sumAmicable += i + factorsi

# Caching results in a dictionary

# sumAmicable = 0
# D = {}
#
# for i in range(2, upperLimit+1):
#     factors = sumOfFactorsPrime(i, primeList)
#     if factors > i:
#         D[i] = factors
#     elif factors < i:
#         if factors in D:
#             if D[factors] == i:
#                 sumAmicable += i + factors
#
# print(sumAmicable)
