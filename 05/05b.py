inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\05\\input05.txt"
with open(inputfile) as f:
    lines = f.readlines()
    
count = 0
i = 0
while i >= 0 and i < len(lines):
    val = int(lines[i])
    next_i = i + val
    if val >= 3:
        lines[i] = val - 1
    else:
        lines[i] = val + 1
    i = next_i
    count += 1

print(count)