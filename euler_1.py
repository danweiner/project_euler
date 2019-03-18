def multiples(n, num1, num2):
    mult_total = 0
    for i in range(num1, n):
        if i % num1 == 0 or i % num2 == 0:
            mult_total += i
    return mult_total

def testMultiples():
    assert multiples(2, 1, 2) == 1
    assert multiples(10, 3, 5) == 23
    print(multiples(1000, 3, 5))
    
testMultiples()