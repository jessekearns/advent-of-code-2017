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

occupied = 0
for i in range(0, 128):
    thisInput = input + '-' + str(i)
    thisHex = knot(thisInput)
    for c in thisHex:
        # It's 11:30 and math is for people who got a good night's sleep
        if c == '0': 
            occupied += 0
        elif c == '1' or c == '2' or c == '4' or c == '8': 
            occupied += 1
        elif c == '3' or c == '5' or c == '6' or c == '9' or c == 'a' or c == 'c': 
            occupied += 2
        elif c == '7' or c == 'b' or c == 'd' or c == 'e':
            occupied += 3
        elif c == 'f':
            occupied += 4
        else:
            print('WTF')
print(occupied)