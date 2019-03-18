D = {1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred'}
count = 0
for i in range(1, 1001):
    thousands = i//1000
    hundreds = i//100
    remainder = i % 100
    if i == 1000:
        count += len(D[thousands])
        count += len('thousand')
        print(D[thousands], 'thousand')
    # Evenly divisible by 100
    elif i >= 100 and remainder == 0:
        count += len(D[hundreds])
        count += len('hundred')
        print(D[hundreds], 'hundred')
    #Account for British English, include 'and' for > 100 not evenly div by 100
    if i >= 100 and remainder != 0:
        count += len(D[hundreds])
        count += len('hundred')
        count += len('and')
        print(D[hundreds], 'hundred', 'and')
    # All numbers < 100, and all nums > 100 not evenly divisible by 100
    if remainder != 0:
        if remainder < 10:
            count += len(D[remainder])
            print(D[remainder])
        elif remainder < 20:
            count += len(D[remainder])
            print(D[remainder])
        elif remainder < 100 and remainder%10 == 0:
            count += len(D[remainder])
            print(D[remainder])
        elif remainder < 100:
            tens = remainder//10
            tens = tens*10
            ones = remainder%10
            count += len(D[tens])
            count += len(D[ones])
            print(D[tens], D[ones])

print(count)
