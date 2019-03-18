
gridSize = 20
grid = [[None for i in range(gridSize+1)] for j in range(gridSize+1)]

for i in range(gridSize):
    grid[i][gridSize] = 1
    grid[gridSize][i] = 1

for i in range(gridSize-1, -1, -1):
    for j in range(gridSize-1, -1, -1):
        grid[i][j] = grid[i+1][j] + grid[i][j+1]

print(grid[0][0])

# for (int i = gridSize - 1; i >= 0; i--) {
#     for (int j = gridSize - 1; j >= 0; j--) {
#         grid[i, j] = grid[i+1, j] + grid[i, j+1];
#     }
# }
