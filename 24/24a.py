def GetMatrixFromList(list):
    componentMatrix = []
    for i in range(max + 1):
        componentMatrix.append([])
        for j in range(max + 1):
            componentMatrix[i].append(0)

    for component in list:
        componentMatrix[component[0]][component[1]] += 1
        componentMatrix[component[1]][component[0]] += 1

    return componentMatrix

def GetStrengthOfBridge(bridge):
    strength = 0
    for component in bridge:
        strength += component[0]
        strength += component[1]
    return strength

def GetNextComponentCandidates(current, matrix):
    candidates = []
    row = matrix[current]
    # Search high to low - greedy algorithm
    for col in reversed(range(len(row))):
        availableNumber = row[col]
        if availableNumber > 0:
            candidates.append((current, col))
    return candidates

def GetStrongestBridge(current, matrix, bridgeSoFar, strengthSoFar):
    candidates = GetNextComponentCandidates(current, matrix)
    if len(candidates) == 0:
        if (strengthSoFar > 1864): # Ran it, plugged in the highest I saw, repeat
            print(bridgeSoFar)
            print("Strength: {0}, length: {1}".format(strengthSoFar, len(bridgeSoFar)))
        return []

    bestStrength = 0
    bestBridge = []

    for candidate in candidates:
        nextConnection = candidate[1]
        candidateStrength = GetStrengthOfBridge([(current, nextConnection)])
        matrix[current][nextConnection] -= 1
        matrix[nextConnection][current] -= 1
        candidateBridge = GetStrongestBridge(nextConnection, matrix, bridgeSoFar + [(current, nextConnection)], strengthSoFar + candidateStrength)
        matrix[current][nextConnection] += 1
        matrix[nextConnection][current] += 1
        candidateStrength = GetStrengthOfBridge(candidateBridge)
        if (candidateStrength > bestStrength):
            bestStrength = candidateStrength
            bestBridge = candidateBridge
        
    return bestBridge


inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\24\\input24.txt"
with open(inputfile) as f:
    lines = f.readlines()

components = []
max = 0
for line in lines:
    pair = (int(line.split('/')[0]), int(line.split('/')[1]))
    if pair[0] > max:
        max = pair[0]
    if pair[1] > max:
        max = pair[1]
    components.append(pair)

componentMatrix = GetMatrixFromList(components)
bridge = GetStrongestBridge(0, componentMatrix, [], 0)
strength = GetStrengthOfBridge(bridge)

print(bridge)
print("Strength: {0}, length: {1}".format(strength, len(bridge)))