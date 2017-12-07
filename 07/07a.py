inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\07\\input07.txt"
with open(inputfile) as f:
    lines = f.readlines()
weights = {}
children = {}
parents = {}
for line in lines:
    cleanLine = line.replace("\n", "").replace("->", "").replace("(", "").replace(")", "").replace(",", "").replace("  ", " ")
    tokens = cleanLine.split(" ")
    name = tokens[0]
    weight = int(tokens[1])
    thisChildren = []
    for i in range(2, len(tokens)):
        thisChildren.append(tokens[i])
        parents[tokens[i]] = name
    weights[name] = weight
    children[name] = thisChildren


key = next(iter(parents))
while True:
    if key in parents:
        key = parents[key]
    else:
        print(key)
        break
