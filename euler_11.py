nums = '''10 11 14 18
30 45 89 65
53 45 43 23'''

L = nums.split('\n')


for row in range(len(L)):
    # Split to rows
    L[row] = L[row].split(" ")
    rowLength = len(L[row])
    colTotal = 0
    for col in range(len(L[row])):
        # Convert from str to int
        L[row][col] = int(L[row][col])
        if col < rowLength - 3:
            colTotal = int(L[row][col]) + int(L[row][col+1])
            print(L[row][col], L[row][col+1], colTotal)
            


    