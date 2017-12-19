stepCount = 314 # puzzle input
numSteps = 2017
array = [0]
step = 1
pos = 0

while step <= numSteps:
    pos += stepCount
    pos %= step
    newArr = array[0:pos+1] + [step] + array[pos+1:]
    array = newArr
    pos += 1
    step += 1

print(array)
print(array[pos + 1])