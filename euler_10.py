def sieve(n):
    primeSum = 0
    a = [True] * n
    a[0] = a[1] = False
    for i in range(2, len(a)):
        if a[i]:
            primeSum += i
        for j in range(i*i, n, i):
            a[j] = False
    return primeSum

print(sieve(2000000))