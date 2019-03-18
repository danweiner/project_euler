limit = 10**999
fib = [None] * 3
print(fib)
fib[0] = 1
fib[2] = 1
i = 0
count = 2
while fib[i] < limit:
    i = (i + 1)%3
    fib[i] = fib[(i + 1)%3] + fib[(i + 2)%3]
    count = count + 1
