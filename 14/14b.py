input = 'hfdlxzhv'

def knot(inputs):
    moreInputs = [17, 31, 73, 47, 23]
    nlist = list(range(0, 256))
    pos = 0
    skip = 0
    for iteration in range(0,64):
        for input in inputs:
            length = ord(input)
            for i in range(0, int((length)/2)):
                index = (i + pos) % 256
                otherIndex = (pos + length - i - 1) % 256
                temp = nlist[index]
                nlist[index] = nlist[otherIndex]
                nlist[otherIndex] = temp
            pos += length
            pos += skip
            pos %= 256
            skip += 1
        for length in moreInputs:
            for i in range(0, int((length)/2)):
                index = (i + pos) % 256
                otherIndex = (pos + length - i - 1) % 256
                temp = nlist[index]
                nlist[index] = nlist[otherIndex]
                nlist[otherIndex] = temp
            pos += length
            pos += skip
            pos %= 256
            skip += 1

    xorVals = []
    for i in range(0, 16):
        addVal = i*16
        xSum = nlist[addVal]
        for j in range(1, 16):
            xSum = xSum ^ nlist[addVal + j]
        xorVals.append(xSum)

    hexTotal = ""
    for x in xorVals:
        hexOutput = str(hex(x)).replace('0x', '')
        if (len(hexOutput) == 1):
            hexOutput = '0' + hexOutput
        hexTotal += hexOutput
    return hexTotal

def processGroup(grid, i, j):
    if (grid[i][j]):
        grid[i][j] = False
        print("Group includes {0}, {1}".format(i, j))
        if i > 0:
            processGroup(grid, i - 1, j)
        if i < 127:
            processGroup(grid, i + 1, j)
        if j > 0:
            processGroup(grid, i, j - 1)
        if j < 127:
            processGroup(grid, i, j + 1)

def countGroups(grid):
    groups = 0
    for i in range(0, 128):
        for j in range(0, 128):
            if grid[i][j]:
                processGroup(grid, i, j)
                print("Group found at {0}, {1}".format(i, j))
                groups += 1
                print("Total is now {0}\n".format(groups))
    return groups

grid = []
for i in range(0, 128):
    thisInput = input + '-' + str(i)
    thisHex = knot(thisInput)
    scale = 16 ## equals to hexadecimal
    num_of_bits = 128
    thisBin = bin(int(thisHex, scale))[2:].zfill(num_of_bits)
    row = []
    for j in range(0, 128):
        if str(thisBin)[j] == '1':
            row.append(True)
        else:
            row.append(False)
    grid.append(row)

print(countGroups(grid))