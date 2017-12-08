inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\08\\input08.txt"
with open(inputfile) as f:
    lines = f.readlines()
registers = {}
max = -999

for line in lines:
    tokens = line.replace("\n", "").split(" ")
    regName = tokens[0]
    addVal = int(tokens[2])
    if (tokens[1] == "dec"):
        addVal *= -1
    condName = tokens[4]
    cond = tokens[5]
    condVal = int(tokens[6])

    if (condName not in registers):
        registers[condName] = 0
    if (regName not in registers):
        registers[regName] = 0
    
    if  (cond == "==" and registers[condName] == condVal ) or \
        (cond == "<=" and registers[condName] <= condVal ) or \
        (cond == ">=" and registers[condName] >= condVal ) or \
        (cond == "!=" and registers[condName] != condVal ) or \
        (cond == ">" and registers[condName] > condVal ) or \
        (cond == "<" and registers[condName] < condVal ):
        registers[regName] += addVal
    
    if (registers[regName] > max):
        max = registers[regName]




print("\nMax: {0}".format(max))