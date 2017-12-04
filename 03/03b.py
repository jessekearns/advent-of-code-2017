input = 265149

# Initialize our lookup table of index to value, and our counters for generating the spiral
spiralVals = [0, 1] # 1->1, 2 -> 1, 3 -> 2, 4 -> 4, etc.
spiralCoordinates = {} # (0, 0) -> 1, (1, 0) -> 2, etc.
spiralCoordinates[(0, 0)] = 1
currx = 1
curry = 0
current = 2
currentval = 1
edgeLength = 2
stepsInDirection = 1
directionChanges = 0

# Iteratively store each index's value and coordinates
while currentval < input:
    spiralCoordinates[(currx, curry)] = current

    print("Index {0} at {1}, {2} with edge {3} and steps {4}".format(current, currx, curry, edgeLength, stepsInDirection))
    
    # Get list of 8 adjacent points
    adjacentPoints = []
    adjacentPoints.append((currx + 1, curry))
    adjacentPoints.append((currx + 1, curry + 1))
    adjacentPoints.append((currx, curry + 1))
    adjacentPoints.append((currx - 1, curry + 1))
    adjacentPoints.append((currx - 1, curry))
    adjacentPoints.append((currx - 1, curry - 1))
    adjacentPoints.append((currx, curry - 1))
    adjacentPoints.append((currx + 1, curry - 1))

    # Get the values for any populated points and sum them for this value
    currentval = 0
    for pair in adjacentPoints:
        if pair in spiralCoordinates:
            adjacentIndex = spiralCoordinates[pair]
            adjacentVal = spiralVals[adjacentIndex]
            print("Index {0} is adjacent to {1}; adding {2}".format(current, adjacentIndex, adjacentVal))
            currentval += adjacentVal
    spiralVals.append(currentval)

    print("Index {0} stores value {1}\n".format(current, currentval))
    

    # Increment position info

    # Special Case - Completed a full square, increment edge length and move right
    if (stepsInDirection == 0 and directionChanges % 4 == 0):
        currx += 1
        edgeLength += 2
    # Moving up - increment Y
    elif (directionChanges % 4 == 0):
        curry += 1
    # Moving left - decrement X
    elif (directionChanges % 4 == 1):
        currx -= 1
    # Moving down - decrement Y
    elif (directionChanges % 4 == 2):
        curry -= 1
    # Moving right - increment X
    elif (directionChanges % 4 == 3):
        currx += 1

    # Increment to next index and coordinates
    stepsInDirection += 1
    
    # Turn the corner, change direction
    if (stepsInDirection >= edgeLength and edgeLength > 0):
        stepsInDirection = 0
        directionChanges += 1
    current += 1