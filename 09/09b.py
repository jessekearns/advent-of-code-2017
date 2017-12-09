inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\09\\input09.txt"
with open(inputfile) as f:
    lines = f.readlines()
stream = lines[0]

totalScore = 0
currentScore = 0
isGarbage = False
shouldIgnore = False
garbageCount = 0

for character in stream:
    if (shouldIgnore): 
        shouldIgnore = False
        continue
    if (character == "!"):
        shouldIgnore = True
        continue
    if (isGarbage):
        if character == ">":
            isGarbage = False
            continue
        else : 
            garbageCount += 1
            continue
    if character == "<":
        isGarbage = True
    if character == "{":
        currentScore += 1
    if character == "}":
        totalScore += currentScore
        currentScore -= 1




print(garbageCount)