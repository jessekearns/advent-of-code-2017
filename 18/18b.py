import collections

def set(x, y, registers):
    registers[x] = y

def increase(x, y, registers):
    registers[x] += y

def multiply(x, y, registers):
    registers[x] *= y

def modulo(x, y, registers):
    registers[x] %= y

def jump(x, y, registers, position):
    xVal = 0
    try:
        xVal = int(x)
    except:
        xVal = registers[x]
    if xVal > 0:
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



inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\18\\input18.txt"
with open(inputfile) as f:
    lines = f.readlines()

registers0 = collections.defaultdict(int)
registers0['p'] = 0
registers1 = collections.defaultdict(int)
registers1['p'] = 1

sendVals0 = []
sendVals1 = []

sendCount0 = 0
sendCount1 = 0

position0 = 0
position1 = 0

shouldCheckForDeadlock = False
currentProgramIsZero = True
# True = 0
# False = 1

while (position0 >= 0 and position0 < len(lines)) or (position1 >= 0 and position1 < len(lines)):
    if currentProgramIsZero:
        position = position0
    else:
        position = position1
    registers = registers1
    if (currentProgramIsZero): registers = registers0
    args = lines[position].replace('\n', '').split(' ')
    command = args[0]
    x = args[1]
    try:
        secondArg = args[2]
        y = parseSecondArg(secondArg, registers)
    except:
        y = 0

    if command == 'snd':
        if(currentProgramIsZero):
            sendCount0 += 1
            sendVals0.append(registers[x])
        else:
            sendCount1 += 1
            sendVals1.append(registers[x])
    elif command == 'set':
        set(x, y, registers)
    elif command == 'add':
        increase(x, y, registers)
    elif command == 'mul':
        multiply(x, y, registers)
    elif command == 'mod':
        modulo(x, y, registers)
    elif command == 'rcv':
        if currentProgramIsZero:
            if len(sendVals1) == 0:
                if shouldCheckForDeadlock:
                    print("Deadlocked")
                    break
                shouldCheckForDeadlock = True
                currentProgramIsZero = False
                continue
            registers0[x] = sendVals1.pop(0)
        else:
            if len(sendVals0) == 0:
                if shouldCheckForDeadlock:
                    print("Deadlocked")
                    break
                shouldCheckForDeadlock = True
                currentProgramIsZero = True
                continue
            registers1[x] = sendVals0.pop(0)
    elif command == 'jgz':
        if currentProgramIsZero:
            position0 = jump(x, y, registers, position0)
        else:
            position1 = jump(x, y, registers, position1)
    else:
        print("{0} command not recognized".format(command))

    if currentProgramIsZero:
        position0 += 1
    else:
        position1 += 1

    shouldCheckForDeadlock = False

    # print("Status:")
    # for r in registers0:
    #     print("{0}: {1}".format(r, registers[r]))
    # print("-----")
    # for r in registers1:
    #     print("{0}: {1}".format(r, registers[r]))
    # print("")

print("\nFinal Status:")
for r in registers:
    print("{0}: {1}".format(r, registers[r]))
print("Program 0 send count: {0}".format(sendCount0))
print("Program 1 send count: {0}".format(sendCount1))