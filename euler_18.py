import math

def readInput(fileName):
    lines = 0
    r = open(fileName, 'r')
    L = r.readlines()
    for line in L:
        lines += 1
    # create 2D array
    inputTriangle = [[0] * lines for i in range(lines)]
    j = 0
    # input numbers to array, with padding for zeros
    for line in L:
        linePieces = line.strip('\n').split(' ')
        for i in range(len(linePieces)):
            inputTriangle[j][i] = int(linePieces[i])
        j = j + 1

    r.close()
    return inputTriangle

fileName = 'euler_18.txt'
inputTriangle = readInput(fileName)

#Dynamic Programming approach
lines = len(inputTriangle[0])
for i in range(lines-2, -1, -1):
    for j in range(0, i+1):
        inputTriangle[i][j] += max(inputTriangle[i+1][j], inputTriangle[i+1][j+1])
        print(inputTriangle[i][j])
print(inputTriangle[0][0])

#Brute force approach
# posSolutions = int(math.pow(2, len(inputTriangle[0])-1))
# largestSum = 0
# tempSum = 0
#
# for i in range(posSolutions+1):
#     tempSum = inputTriangle[0][0]
#     index = 0
#     for j in range(len(inputTriangle[0])-1):
#         index = index + (i >> j & 1);
#         tempSum += inputTriangle[j+1][index]
#     if tempSum > largestSum:
#         largestSum = tempSum
#
# print(largestSum)
