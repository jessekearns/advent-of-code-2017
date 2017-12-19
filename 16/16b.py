def spin(arr, num):
    standing = arr[0:(16-num)]
    moving = arr[16-num:16]
    return moving + standing
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    return arr

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\16\\input16.txt"
with open(inputfile) as f:
    moves = f.readlines()[0].split(',')
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
arrangements = {}
totalIterations = 1000000000

iter = 0
finalIndex = 0
loopFound = False
while not loopFound and iter < totalIterations:
    for move in moves:
        if move[0] == 's':
            num = int(move[1:])
            arr = spin(arr, num)
        elif move[0] == 'x':
            first = int(move[1:].split('/')[0])
            second = int(move[1:].split('/')[1])
            arr = swap(arr, first, second)
        # even number of partner swaps = same place after a billion so ignore

    thisArrangement = ''
    for p in arr: 
        thisArrangement += p

    if thisArrangement in arrangements:
        print("cycle found: {0} to {1}".format(iter, arrangements[thisArrangement]))
        loopLength =  iter - arrangements[thisArrangement]
        finalIndex = (totalIterations % loopLength)
        print(finalIndex)
        loopFound = True
        break
    else:
        arrangements[thisArrangement] = iter

    iter += 1

# Get the change after one iteration
# positionList = []
# for i in range(16):
#     for j in range(16):
#         if arr[j] == originalArr[i]:
#             offset = j - i
#             if(offset < 0): offset += 16
#             positionList.append(offset)

# # Multiply the offsets by a billion and apply
# for i in range(16):
#     pos = positionList[i]
#     newOffset = pos * 1000000000
#     newPos = (newOffset + i) % 16
#     arr[newPos] = originalArr[i]


print(arrangements)
for key in arrangements:
    if(arrangements[key] == finalIndex):
        print(key)