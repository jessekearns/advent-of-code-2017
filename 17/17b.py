stepCount = 314 # puzzle input
numSteps = 50000000
step = 1
pos = 0
currentNext = 0

while step <= numSteps:
    pos += stepCount
    pos %= step
    if pos == 0:
        currentNext = step
    pos += 1
    step += 1

print(currentNext)