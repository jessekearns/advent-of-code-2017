totalBursts = 10000000
inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\22\\input22.txt"
with open(inputfile) as f:
    lines = f.readlines()

map = {}
length = len(lines)
for i in range(length):
    for j in range(length):
        if list(lines[i])[j] == '#':
            map[(i, j)] = 2
        else:
            map[(i, j)] = 0

iA = int(length/2)
jA = int(length/2)
direction = 1 # Up
infections = 0
for iteration in range(totalBursts):
    if not (iA, jA) in map:
        map[(iA, jA)] = 0
    nodeState = map[(iA, jA)]

    # Turn
    if nodeState == 0:
        # clean - left
        direction += 1
    elif nodeState == 1:
        # weakened - no turn
        direction += 0
    elif nodeState == 2:
        # infected - right
        direction += 0
    elif nodeState == 3:
        # flagged - revers
        direction += 2
    direction %= 4
    
    # Infect
    map[(iA, jA)] = (nodeState + 1) % 4
    if (nodeState == 1):
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