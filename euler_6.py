def sum_square_dif(L):
    sum_of_squares = 0
    square_of_sums = 0
    for i in L:
        sum_of_squares = sum_of_squares + i*i
        square_of_sums = square_of_sums + i
    
    square_of_sums = square_of_sums**2
    sum_square_diff = square_of_sums - sum_of_squares
    return sum_square_diff
    
L = list(range(1, 101))
print(sum_square_dif(L))