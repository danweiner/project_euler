def fib(n):
    a, b = 0, 1
    total = 0
    while a < n+1:
        a, b = b, a+b
        if a%2 == 0:
            total += a
    return total


def testFibEvens():
    assert fib(8) == 10
    assert fib(34) == 44
    print(fib(4000000))

 
 
testFibEvens()