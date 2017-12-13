inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\12\\input12.txt"
with open(inputfile) as f:
    lines = f.readlines()

inputTable = {}
belongsToCurrentGroup = {}
unProcessed = []
processed = []
needsToBeProcessed = []
groups = 0

for line in lines:
    segs = line.split(' <-> ')
    id = int(segs[0])
    connections = []
    for connection in segs[1].split(', '):
        connections.append(int(connection))
    belongsToCurrentGroup[id] = False
    inputTable[id] = connections
    unProcessed.append(id)

while len(unProcessed) > 0:
    for key in belongsToCurrentGroup:
        belongsToCurrentGroup[key] = False
    needsToBeProcessed.append(unProcessed.pop())
    while len(needsToBeProcessed) > 0:
        current = needsToBeProcessed.pop()
        belongsToCurrentGroup[current] = True
        for connection in inputTable[current]:
            if connection not in processed:
                needsToBeProcessed.append(connection)
            if (connection in unProcessed):
                unProcessed.remove(connection)
        if current not in processed:
            processed.append(current)
    groups += 1
  
print (groups)