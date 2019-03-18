name_file = open('p022_names.txt', 'r')
f = name_file.readlines()
names = []
for name in f:
    name = name.strip(" ").split(',')
    names = names + name
print(names)
d = {}
letters = 'ABCDEFGHIJKLMNOPRQSTUVWXYZ'
for c in letters:
    d[c] = (ord(c)%ord('A'))+1

sorted_names = sorted(names)

total = 0
for i, name in enumerate(sorted_names):
    sum_letters = 0
    print('i', i, 'name', name)
    for c in name:
        if c.isalpha():
        #add value of chars in name
            sum_letters += d[c]

    total = total + (sum_letters * (i+1))

print(total)
