inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\10\\input10.txt"
with open(inputfile) as f:
    lines = f.readlines()
inputs = lines[0]
moreInputs = [17, 31, 73, 47, 23]
list = list(range(0, 256))
pos = 0
skip = 0

for iteration in range(0,64):
    for input in inputs:
        length = ord(input)
        for i in range(0, int((length)/2)):
            index = (i + pos) % 256
            otherIndex = (pos + length - i - 1) % 256
            temp = list[index]
            list[index] = list[otherIndex]
            list[otherIndex] = temp
        pos += length
        pos += skip
        pos %= 256
        skip += 1
    for length in moreInputs:
        for i in range(0, int((length)/2)):
            index = (i + pos) % 256
            otherIndex = (pos + length - i - 1) % 256
            temp = list[index]
            list[index] = list[otherIndex]
            list[otherIndex] = temp
        pos += length
        pos += skip
        pos %= 256
        skip += 1

xorVals = []
for i in range(0, 16):
    addVal = i*16
    xSum = list[addVal]
    for j in range(1, 16):
        xSum = xSum ^ list[addVal + j]
    xorVals.append(xSum)

hexTotal = ""
for x in xorVals:
    hexTotal += str(hex(x)).replace('0x', '')
    print(str(hex(x)).replace('0x', ''))

print(hexTotal)