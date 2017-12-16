def spin(arr, num):
    standing = arr[0:(16-num)]
    moving = arr[16-num:16]
    return moving + standing
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    return arr
def partner(arr, first, second):
    firstIndex = 0
    secondIndex = 0
    for i in range(16):
        if (first == arr[i]):
            firstIndex = i
        if (second == arr[i]):
            secondIndex = i
    return swap(arr, firstIndex, secondIndex)

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\16\\input16.txt"
with open(inputfile) as f:
    moves = f.readlines()[0].split(',')
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

for aFrickinBillion in range(1000000000):
    for move in moves:
        if move[0] == 's':
            num = int(move[1:])
            arr = spin(arr, num)
        elif move[0] == 'x':
            first = int(move[1:].split('/')[0])
            second = int(move[1:].split('/')[1])
            arr = swap(arr, first, second)
        elif move[0] == 'p':
            first = move[1:].split('/')[0]
            second = move[1:].split('/')[1]
            arr = partner(arr, first, second)

output = ''
for p in arr: 
    output += p
print(output)