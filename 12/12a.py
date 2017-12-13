inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\12\\input12.txt"
with open(inputfile) as f:
    lines = f.readlines()

inputTable = {}
zeroGroup = {}
processed = []
needsToBeProcessed = []

for line in lines:
    segs = line.split(' <-> ')
    id = int(segs[0])
    connections = []
    for connection in segs[1].split(', '):
        connections.append(int(connection))
    zeroGroup[id] = False
    inputTable[id] = connections

needsToBeProcessed.append(0)
while len(needsToBeProcessed) > 0:
    current = needsToBeProcessed.pop()
    zeroGroup[current] = True
    for connection in inputTable[current]:
        if connection not in processed:
            needsToBeProcessed.append(connection)
    if current not in processed:
        processed.append(current)
  
print (len(processed))