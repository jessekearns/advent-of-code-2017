inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\02\\input2.txt"
with open(inputfile) as f:
    rows = f.readlines()
checksum = 0
for row in rows:
    rowmin = 99999999
    rowmax = 0
    for stringnum in row.split('\t'):
        num = int(stringnum)
        if num > rowmax:
            rowmax = num
        if num < rowmin:
            rowmin = num
    rowsum = rowmax - rowmin
    checksum += rowsum

print(checksum)