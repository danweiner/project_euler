def collatz(n):
    maxCount = 0
    maxNum = n
    count = 0
    for i in range(n, 1, -1):
        divider = i
        while divider > 1:
            if divider%2 == 0:
                divider = divider //2
                count += 1
            else:
                divider = divider * 3 + 1
                count += 1
        if count > maxCount:
            maxCount = count
            count = 0
            maxNum = i
            print(maxNum, maxCount)
        count = 0
    return maxNum, maxCount
