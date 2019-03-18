months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(sum(months))
nonLeapStart = sum(months)%364
print(len(months))
 #monday - not a leap year
# start1901 = start1900 +  nonLeapStart #tuesday
# print(start1901)
# #in 1901...
# firstOfFeb = (start1901+months[0])%28
# print(firstOfFeb)
start = 2 # starts on a Tuesday
sundays = 0
for i in range(1901, 2001):
    for j in range(len(months)):
        if j == 1:
            if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
                start = ((start + months[j]+1)%28)%7
        else:
            start = ((start + months[j])%28)%7
        if start == 0:
            sundays += 1

print(sundays)
