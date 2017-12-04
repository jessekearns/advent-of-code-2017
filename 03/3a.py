input = 265149
myx = 0
myy = 0

# Find nearest odd square
nearsqrt = int(input**(.5))
if nearsqrt % 2 == 0:
    nearsqrt -= 1
nearsq = nearsqrt**2
distsq = input - nearsq
sqx = (nearsqrt - 1)/2
sqy = -(nearsqrt - 1)/2
print ("The nearest odd square is {0}, square of {1}, located at {2},{3}".format(nearsq, nearsqrt, sqx, sqy))

# Count up to our input number
if (nearsq == input):
    myx = sqx
    myy = sqy
else :
    current = nearsq + 1
    currx = sqx + 1
    curry = sqy
    directionChanges = 0
    stepsInDirection = 1
    while (current < input):
        current += 1
        stepsInDirection += 1
        # Moving up - increment Y
        if (directionChanges == 0):
            curry += 1
        # Moving left - decrement X
        if (directionChanges == 1):
            currx -= 1
        # Moving down - decrement Y
        if (directionChanges == 2):
            curry -= 1
        # Moving right - increment X
        if (directionChanges == 3):
            currx += 1

        # Track direction
        if (stepsInDirection > nearsqrt):
            stepsInDirection = 0
            directionChanges += 1
    myx = currx
    myy = curry
print ("Input {0} is located at {1}, {2}".format(input, myx, myy))

# Get the Manhattan distance from the origin
mandist = abs(myx) + abs (myy)
print ("Input {0} is {1} steps away from 1".format(input, mandist))