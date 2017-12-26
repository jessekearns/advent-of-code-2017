import collections
totalSteps = 12964419

def checksum(tape):
    total = 0
    for key in tape:
        total += tape[key]
    return total

# Parsing is for people who don't do their puzzles on Christmas morning
def a(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        return (1, 'b')
    else:
        tape[pos] = 0
        return (1, 'f')

# moves left until it finds a one, then C
def b(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 0
        return (-1, 'b')
    else:
        tape[pos] = 1
        return (-1, 'c')

def c(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        return (-1, 'd')
    else:
        tape[pos] = 0
        return (1, 'c')

def d(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        return (-1, 'e')
    else:
        tape[pos] = 1
        return (1, 'a')

def e(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        return (-1, 'f')
    else:
        tape[pos] = 0
        return (-1, 'd')

def f(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        return (1, 'a')
    else:
        tape[pos] = 0
        return (-1, 'e')


state = 'a'
steps = 0
tape = collections.defaultdict(int)
position = 0
while steps < totalSteps:
    if state == 'a':
        retval = a(tape, position)
    elif state == 'b':
        retval = b(tape, position)
    elif state == 'c':
        retval = c(tape, position)
    elif state == 'd':
        retval = d(tape, position)
    elif state == 'e':
        retval = e(tape, position)
    elif state == 'f':
        retval = f(tape, position)

    position += retval[0]
    state = retval[1]
    steps += 1

result = checksum(tape)
print("After {0} steps, the checksum is {1}".format(steps, result))