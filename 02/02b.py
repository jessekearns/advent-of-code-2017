inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\02\\input2.txt"
with open(inputfile) as f:
    rows = f.readlines()
checksum = 0
for row in rows:
    rowsum = 0
    rownums = row.split('\t')
    rowlen = len(rownums)
    for i in range(0, rowlen-2):
        num1 = int(rownums[i])
        for j in range(i+1, rowlen):
            num2 = int(rownums[j])
            maxnum = max(num1, num2)
            minnum = min(num1, num2)
            if maxnum % minnum == 0:
                rowsum = int(maxnum / minnum)
    if rowsum > 0:
        checksum += rowsum
    else:
        print(row)

print(checksum)