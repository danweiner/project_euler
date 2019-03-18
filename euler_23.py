import math
from euler_21 import ESieve, sumOfFactorsPrime

# find all abundant numbers
# create and mark all numbers which can be created as the sum
# of two abundant numbers
# sum up all non-marked numbers

limit = 28123
abundant = []
primeList = ESieve(int(math.sqrt(limit)))
sum = 0

# find all abundant numbers
for i in range(2, limit+1):
    if sumOfFactorsPrime(i, primeList) > i:
        abundant.append(i)

# create all sums of numbers
canBeWrittenAsAbundant = [False] * (limit+1)
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] <= limit:
                canBeWrittenAsAbundant[abundant[i] + abundant[j]] = True
            else:
                break

# sum numbers which are not sums of two abundant
for i in range(1, limit+1):
    if not canBeWrittenAsAbundant[i]:
        sum += i

print(sum)                    
