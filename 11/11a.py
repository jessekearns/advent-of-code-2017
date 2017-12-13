inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\11\\input11.txt"
with open(inputfile) as f:
    lines = f.readlines()
inputs = lines[0].split(',')
n = 0
ne = 0
se = 0
for input in inputs:
    if input == 's':
        n -= 1
    elif input == 'n':
        n += 1
    elif input == 'ne':
        ne += 1
    elif input == 'sw':
        ne -= 1
    elif input == 'se':
        se += 1
    elif input == 'nw':
        se -= 1

print('{0}, {1}, {2}: {3}'.format(n, ne, se, (n+ne+se)))