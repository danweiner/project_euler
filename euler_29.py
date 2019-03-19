# Solve with dictionary or a set

s = set()

for a in range(2, 101):
    for b in range(2, 101):
        combo = a**b
        # if combo not in d:
        #     d[combo] = 1
        # else:
        #     d[combo] += 1
        s.add(combo)


print(len(s))
