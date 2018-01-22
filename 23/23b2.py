def initialize():
    global b
    global c
    global d
    global e
    global f
    global g
    global h

    b = 81
    c = 81
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0

def outestLoop():
    global b
    global c
    global d
    global e
    global f
    global g
    global h

    f = 1
    d = 2

    outerLoop()
    while (g != 0):
        outerLoop()

    if (f == 0):
        h += 1

    g = b
    g -= c
    if (g != 0):
        b += 17

def outerLoop():
    global b
    global c
    global d
    global e
    global f
    global g
    global h

    e = 2
    innerLoop()
    while (g != 0):
        innerLoop()
    d += 1
    g = d
    g -= b

def innerLoop():
    global b
    global c
    global d
    global e
    global f
    global g
    global h

    g = d
    g *= e
    g -= b
    if (g == 0):
        f = 0
    e += 1
    g = e
    g -= b

# Just going to try converting to Python so I can optimize

debug = True
initialize()

if (not debug):
    b *= 100
    b += 100000
    c = b
    c += 17000

outestLoop()
while (g != 0):
    outestLoop()

print("b: {0}".format(b))
print("c: {0}".format(c))
print("d: {0}".format(d))
print("e: {0}".format(e))
print("f: {0}".format(f))
print("g: {0}".format(g))
print("h: {0}".format(h))