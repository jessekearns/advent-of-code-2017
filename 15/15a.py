currA = 512
currB = 191
iterations = 40000000
multA = 16807
multB = 48271
div = 2147483647
bitAnd = 0b1111111111111111
matches = 0

for i in range(iterations):
    currA = (currA * multA) % div
    currB = (currB * multB) % div

    binA = currA & bitAnd
    binB = currB & bitAnd
    if binA == binB:
        matches += 1

print(matches)