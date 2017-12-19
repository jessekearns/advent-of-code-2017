import collections

def sound(x, registers):
    print('Sounding {0}: {1}'.format(x, registers[x]))
    return registers[x]

def set(x, y, registers):
    registers[x] = y

def increase(x, y, registers):
    registers[x] += y

def multiply(x, y, registers):
    registers[x] *= y

def modulo(x, y, registers):
    registers[x] %= y

def recover(x, registers, previous):
    if (registers[x] != 0):
        print("Recover: {0}".format(previous))

def jump(x, y, registers, position):
    xVal = 0
    try:
        xVal = int(x)
    except:
        xVal = registers[x]
    if xVal > 0:
        print("Jump {0} + {1}".format(position, y))
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

registers = collections.defaultdict(int)
previous = 0
position = 0

while position >= 0 and position < len(lines):
    args = lines[position].replace('\n', '').split(' ')
    command = args[0]
    x = args[1]
    try:
        secondArg = args[2]
        y = parseSecondArg(secondArg, registers)
    except:
        y = 0

    if command == 'snd':
        previous = sound(x, registers)
    elif command == 'set':
        set(x, y, registers)
    elif command == 'add':
        increase(x, y, registers)
    elif command == 'mul':
        multiply(x, y, registers)
    elif command == 'mod':
        modulo(x, y, registers)
    elif command == 'rcv':
        recover(x, registers, previous)
        # Exit after first recover
        position = -1
    elif command == 'jgz':
        position = jump(x, y, registers, position)
    else:
        print("{0} command not recognized".format(command))

    position += 1

    # print("Status:")
    # for r in registers:
    #     print("{0}: {1}".format(r, registers[r]))
    # print("")

print("\nFinal Status:")
for r in registers:
    print("{0}: {1}".format(r, registers[r]))