inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\11\\input11.txt"
with open(inputfile) as f:
    lines = f.readlines()
inputs = lines[0].split(',')
n = 0
ne = 0
se = 0
maxTotalMoves = 0
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

    # Moves SE and SW can be combined into a single move S
    while ne < 0 and se > 0:
        n -= 1 # One more S
        ne += 1 # One less SW
        se -= 1 # One less SE

    # Moves NE and NW can be combined into a single move N
    while ne > 0 and se < 0:
        n += 1 # One more N
        ne -= 1 # One less NE
        se += 1 # One less NW

    # Moves N and SE can be combined into a single move NE
    while n > 0 and se > 0:
        ne += 1 # One more NE
        n -= 1 # One less N
        se -= 1 # One less SE

    # Moves S and NE can be combined into a single move SE
    while n < 0 and ne > 0:
        se += 1 # One more SE
        n += 1 # One less S
        ne -= 1 # One less NE

    # Moves S and NW can be combined into a single move SW
    while n < 0 and se < 0:
        ne -= 1 # One more SW
        n += 1 # One less S
        se += 1 # One less NW

    # Moves N and SW can be combined into a single move NW
    while n > 0 and ne < 0:
        se -= 1 # One more NW
        n -= 1 # One less N
        ne += 1 # One less SW

    totalMoves = (abs(n)+abs(ne)+abs(se))
    #print ('stepping {0}, coordinates({2}, {3}, {4}), {1} steps away from 0'.format(input, totalMoves, n, ne, se))
    if totalMoves > maxTotalMoves:
        maxTotalMoves = totalMoves

print('{0} steps away at most'.format(maxTotalMoves))