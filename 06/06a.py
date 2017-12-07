import copy

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\06\\input06.txt"
with open(inputfile) as f:
    blocks = f.readlines()[0].split('\t')

# Get those inputs as ints
for k in range(0, len(blocks)):
    blocks[k] = int(blocks[k])

# Hey we're playing Mancala
previousArrangements = []
steps = 0
while True:
    previousArrangements.append(copy.deepcopy(blocks))

    # Find max
    maxIndex = 0
    for i in range(0, len(blocks)):
        if (blocks[i] > blocks[maxIndex]):
            maxIndex = i

    # Distribute
    target = (maxIndex + 1) % len(blocks)
    beads = blocks[maxIndex]
    blocks[maxIndex] = 0
    for j in range(0, beads):
        blocks[target] = blocks[target] + 1
        target += 1
        target %= len(blocks)

    # Increment and verify
    steps += 1
    matched = False
    for arrangement in previousArrangements:
        listMatched = True
        for m in range(0, len(blocks)):
            listMatched = listMatched and (blocks[m] == arrangement[m])
        if listMatched :
            matched = listMatched
            break
    if (matched):
        print(blocks)
        print(steps)
        break