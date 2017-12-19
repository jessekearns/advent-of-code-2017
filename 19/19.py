inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\19\\input19.txt"
with open(inputfile) as f:
    rows = f.readlines()
numRows = len(rows)
numCols = len(rows[0])
i = 0 # row number
j = 0 # column number
for startJ in range(numCols):
    c = rows[0][startJ]
    if c == "|":
        j = startJ
direction = 3 # 0 - r, 1 - u, 2 - l, 3 - d
collected = ''
steps = 0

while True:
    # Check for out of bound
    if i < 0 or j < 0 or i >= numRows or j >= numCols:
        break
    
    current = rows[i][j]
    if current == ' ':
        break

    steps += 1

    # Check for turn
    if current == '+':
        if direction == 1 or direction == 3:
            if j > 0 and rows[i][j-1] != ' ':
                direction = 2
            elif j < numCols and rows[i][j+1] != ' ':
                direction = 0
        elif direction == 0 or direction == 2:
            if i > 0 and rows[i-1][j] != ' ':
                direction = 1
            elif i < numCols and rows[i+1][j] != ' ':
                direction = 3

    # Check for letter
    elif current != '|' and current != '-':
        collected += current
    
    # Advance position
    if direction == 0:
        j += 1
    elif direction == 1:
        i -= 1
    elif direction == 2:
        j -= 1
    elif direction == 3:
        i += 1

print(collected)
print(steps)