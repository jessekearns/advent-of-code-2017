# Index is 0 for input, 1 for output
def parseToMatrix(line, index):
    input = line.replace(' ', '').replace('\n', '').split('=>')[index]
    rows = input.split('/')
    newRows = []
    for row in rows:
        newRow = list(row)
        newRows.append(newRow)
    return newRows

def parseToString(matrix):
    output = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output += matrix[i][j]
        output += '/'
    return output[:-1]

def splitMatrix(matrix):
    composedSize = len(matrix)
    innerSize = 0
    outerSize = 0
    if composedSize % 2 == 0:
        innerSize = 2
        outerSize = int(composedSize / 2)
    else:
        innerSize = 3
        outerSize = int(composedSize / 3)
    
    components = []

    for iOut in range(outerSize):
        components.append([])
        for jOut in range(outerSize):
            components[iOut].append([])
            for i in range(innerSize):
                components[iOut][jOut].append([])
                for j in range(innerSize):
                    components[iOut][jOut][i].append(matrix[(iOut * innerSize) + i][(jOut * innerSize) + j])
    return components

def composeMatrix(components):
    outerSize = len(components)
    innerSize = len(components[0][0])
    composedSize = outerSize * innerSize

    # default matrix
    fullMatrix = []
    for i in range(composedSize):
        row = []
        for j in range(composedSize):
            row.append('.')
        fullMatrix.append(row)

    for iOut in range(outerSize):
        for jOut in range(outerSize):
            component = components[iOut][jOut]
            for i in range(innerSize):
                for j in range(innerSize):
                    fullMatrix[(iOut * innerSize) + i][(jOut * innerSize) + j] = component[i][j]

    return fullMatrix

def enhanceMatrix(matrix, dict):
    if len(matrix[0]) > 3:
        components = splitMatrix(matrix)
        for i in range(len(components)):
            for j in range(len(components)):
                components[i][j] = enhanceMatrix(components[i][j], dict)
        return composeMatrix(components)
    else:
        return dict[parseToString(matrix)]

def rotate(input):
    output = list(zip(*input[::-1]))
    return output

def flip(matrix):
    size = len(matrix[0])
    halfSize = int(size/2)
    for i in range(halfSize):
        temp = matrix[i]
        matrix[i] = matrix[size - i - 1]
        matrix[size - i - 1] = temp
    return matrix


inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\21\\input21.txt"
with open(inputfile) as f:
    lines = f.readlines()

initialMatrix = ".#./..#/###"
iterations = 18

dict = {}

for line in lines:
    value = parseToMatrix(line, 1)
    key = parseToMatrix(line, 0)
    
    # Add original key, all rotations and flips, to dict
    dict[parseToString(key)] = value
    for rotation in range(3):
        key = rotate(key)
        dict[parseToString(key)] = value
    key = flip(key)
    dict[parseToString(key)] = value
    for rotation in range(3):
        key = rotate(key)
        dict[parseToString(key)] = value

matrix = parseToMatrix(initialMatrix, 0)

for iteration in range(iterations):
    matrix = enhanceMatrix(matrix, dict)
    #print(parseToString(matrix).replace('/', '\n'))
    onPixels = 0
    offPixels = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == '#'):
                onPixels += 1
            else:
                offPixels += 1
    print ("After {0} iterations, the image will have {1} pixels turned on and {2} turned off".format(iteration + 1, onPixels, offPixels))
    print('')