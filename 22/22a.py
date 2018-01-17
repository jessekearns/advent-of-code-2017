totalBursts = 10000
inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\22\\input22.txt"
with open(inputfile) as f:
    lines = f.readlines()

map = {}
length = len(lines)
for i in range(length):
    for j in range(length):
        infected = (list(lines[i])[j] == '#')
        map[(i, j)] = infected

iA = int(length/2)
jA = int(length/2)
direction = 1 # Up
infections = 0
for iteration in range(totalBursts):
    if not (iA, jA) in map:
        map[(iA, jA)] = False
    infected = map[(iA, jA)]

    # Turn
    if infected:
        # right
        direction += 3
        direction %= 4
    else:
        # left
        direction += 1
        direction %= 4
    
    # Infect
    map[(iA, jA)] = not infected
    if (not infected):
        infections += 1
    
    # Move
    # right
    if (direction == 0):
        jA += 1
    # up
    elif (direction == 1):
        iA -= 1
    # left
    elif (direction == 2):
        jA -= 1
    # down
    elif (direction == 3):
        iA += 1

print("{0} infections after {1} bursts".format(infections, totalBursts))