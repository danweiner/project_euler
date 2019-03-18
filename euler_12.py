import math
def factorize(n):
    factors = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            factors.add(i)
            factors.add(n//i)
    factors = sorted(factors)
    return factors

factors = []
n = 50
while len(factors) < 500:

    triangleNum = ((n+1)*n)//2
    print('triangleNum', triangleNum)
    factors = factorize(triangleNum)
    print('factors', factors)
    n = n + 1

print(factors, len(factors))
