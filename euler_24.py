import itertools
# using built-in library
# perms = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
# millionth = perms[999999]
# s = ''
# for c in millionth:
#     s += str(c)
# print(s)

# Brute force solution
# perm = list(range(10))
# count = 1
# numPerm = 1000000
# def swap(i, j):
#     k = perm[i]
#     perm[i] = perm[j]
#     perm[j] = k
# while count < numPerm:
#     n = len(perm)
#     i = n-1
#     while perm[i-1] >= perm[i]:
#         i = i-1
#         #print('i in first inner while', i)
#     j = n
#     #print('j initial', j)
#     while perm[j-1] <= perm[i-1]:
#         j = j-1
#         #print('j inside while', j)
#     #swap values at position i-1, j-1
#     swap(i-1, j-1)
#     i = i +1
#     j = n
#     #print('i, j after first swap', i, j)
#     while i < j:
#         swap(i-1, j-1)
#         i = i + 1
#         j = j -1
#         #print('i, j after next swap', i, j)
#     count = count + 1
# permNum = ''
# for k in range(len(perm)):
#     permNum = permNum + str(perm[k])

# print('the millionth lex permutation is {}'.format(permNum))

# Using Combinatorics
def factorial(i):
    if i < 0:
        return 0
    p = 1
    for j in range(1, i):
        p *= j
    return p


perm = list(range(10))
n = len(perm)
permNum = ''
remain = 1000000 - 1
numbers = []

for i in range(n):
    numbers.append(i)

for i in range(n):
    j = remain//factorial(n-i)
    remain = remain % factorial(n-i)
    permNum = permNum + str(numbers[j])
    del numbers[j]
    if remain == 0:
        break
for i in range(len(numbers)):
    permNum = permNum + str(numbers[i])

print(permNum)
