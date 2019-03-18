def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a*b)//find_gcd(a, b)

L = list(range(1, 21))
print(L)
num1 = L[0]
num2 = L[1]
lcm = find_lcm(num1, num2)

for i in range(2, len(L)+1):
    if i%2 == 0:
        print(i)
    lcm = find_lcm(lcm, i)
    

print(lcm)