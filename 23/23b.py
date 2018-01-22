import collections

def set(x, y, registers):
    registers[x] = y

def decrease(x, y, registers):
    registers[x] -= y

def multiply(x, y, registers):
    registers[x] *= y

def jump(x, y, registers, position):
    xVal = 0
    try:
        xVal = int(x)
    except:
        xVal = registers[x]
    if xVal != 0:
        #print("Jump {0} + {1}".format(position, y))
        return ((position + y) - 1) # Quick and dirty way to avoid double increment when we add 1
    else:
        return position

def parseSecondArg(y, registers):
    try:
        yVal = int(y)
    except:
        yVal = registers[y]
    return yVal

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\23\\input23.txt"
with open(inputfile) as f:
    lines = f.readlines()

registers = collections.defaultdict(int)
registers['a'] = 1

position = 0
mulCount = 0

while (position >= 0 and position < len(lines) and mulCount <= 6241):
    #print("{0}: {1}".format(position+1, lines[position].replace('\n', '')))
    args = lines[position].replace('\n', '').split(' ')
    command = args[0]
    x = args[1]
    try:
        secondArg = args[2]
        y = parseSecondArg(secondArg, registers)
    except:
        y = 0

    if command == 'set':
        set(x, y, registers)
    elif command == 'sub':
        # Pretty sure this is wrong Prevent cycle 9-32
        # if (position == 30):
        #     decrease(x, registers['g'], registers)
        # else:
        decrease(x, y, registers)
    elif command == 'mul':
        multiply(x, y, registers)
        mulCount += 1
    elif command == 'jnz':
        # Prevent cycle 12-20
        if (position == 19):
            #print("Short circuiting command 20 by adding g to e and setting g to 0")
            gVal = registers['g']
            registers['e'] -= gVal
            registers['g'] = 0
        # Prevent Cycle 11-24
        if (position == 23):
            #print("Short circuiting command 24 by adding g to d and setting g to 0")
            gVal = registers['g']
            registers['d'] -= gVal
            registers['g'] = 0
        position = jump(x, y, registers, position)
    else:
        print("{0} command not recognized".format(command))
    
    position += 1

    # print("{0}: {1}".format("Pos", position))
    # for r in registers:
    #     print("{0}: {1}".format(r, registers[r]))
    # print('')

print("\nFinal Status:")
for r in registers:
    print("{0}: {1}".format(r, registers[r]))