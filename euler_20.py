fact = 1
n = 100
for i in range(1, n+1):
    fact = fact*i
print(fact)
total = 0
for c in str(fact):
    total += int(c)
print(total)
