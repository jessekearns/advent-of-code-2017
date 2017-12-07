def computeWeight(name, weights, children):
    weightSoFar = weights[name]
    for child in children[name]:
        weightSoFar += computeWeight(child, weights, children)
    return weightSoFar

def printTreeWeights(name, cumulativeWeights, children, weights, indentation):
    print("{2}{0}: {1}, {3}".format(name, cumulativeWeights[name], indentation, weights[name]))
    for child in children[name]:
        printTreeWeights(child, cumulativeWeights,children, weights, indentation + "   ")

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\07\\input07.txt"
with open(inputfile) as f:
    lines = f.readlines()
weights = {}
cumulativeWeights = {}
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

for key in children:
    cumulativeWeights[key] = computeWeight(key, weights, children)

for key in children:
    thisChildren = children[key]
    if (len(thisChildren) > 0):
        prevWeight = -1
        for child in thisChildren:
            if child in cumulativeWeights:
                childWeight = cumulativeWeights[child]
            else:
                childWeight = weights[child]
            if prevWeight == -1:
                prevWeight = childWeight
            else:
                if prevWeight != childWeight:
                    print("{0} is unbalanced".format(key))
                    printTreeWeights(key, cumulativeWeights, children, weights, "")
                    print()
                    break

