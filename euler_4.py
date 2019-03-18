def isPal(n):
    return str(n) == str(n)[::-1]
    
def largestPalProduct(high, low):
    maxVal = 0
    for i in range(high, low, -1):
        for j in range(high, i-1, -1):
            prod = i*j
            if prod > maxVal and isPal(prod):
                maxVal = prod
    return (maxVal, high-i, high-j)
    
    
    
def testLargestPal():
    #assert largestPalProduct(99, 0) == (91, 99)
    print(largestPalProduct(999, 0))

testLargestPal()
print(924*962)
