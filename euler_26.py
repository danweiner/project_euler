sequence = 0
answer = 0
for i in range(1000, 1, -1):
    if sequence >= i:
        break

    foundRemainders = [0] * i
    numerator = 1
    position = 0
    while foundRemainders[numerator] == 0 and numerator != 0:
        foundRemainders[numerator] = position
        numerator = numerator * 10
        numerator = numerator % i
        position = position + 1

    if position - foundRemainders[numerator] > sequence:
        sequence = position - foundRemainders[numerator]
        answer = i

print(sequence, answer)
