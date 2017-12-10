inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\10\\input10.txt"
with open(inputfile) as f:
    lines = f.readlines()
inputs = lines[0].split(',')
list = list(range(0, 256))
pos = 0
skip = 0

for input in inputs:
    length = int(input)
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
    print(list)
    print(pos)
    print(skip)
    print()

print(list)
print(list[0]*list[1])


