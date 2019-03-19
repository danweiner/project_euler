spiral_start = 1
num_spirals = 1001
num_loops = num_spirals // 2
total_spiral = 1
for i in range(num_loops):
    for j in range(4):
        spiral_start = spiral_start + 2*(i+1)
        total_spiral = total_spiral + spiral_start

print('total_spiral', total_spiral)
