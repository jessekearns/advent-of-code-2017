import math

# Converting the whole thing to Python and then working through to optimize

# Thanks Stack Overflow
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def outestLoop(b, c):
    candidates = []
    candidates.append(b)
    while (b < c):
        b += 17
        if (b > c):
            print("Bogus input!")
        else:
            candidates.append(b)
        
    
    h = 0
    for candidate in candidates:
        if (not is_prime(candidate)):
            h += 1

    return h
              

def outerLoop(b, d, f):
    # set d and e to b
    # set g to 0
    # set f to 0 if b is divisible by any number 2 - b-1
    # --> if b is not prime set f to 0
    # Inner loop
    if (is_prime(b)):
        f = 0

    return(b, b, f, 0)

def innerLoop(b, d, e):
    # Loop - Set e to b, g to 0, and f to zero iff d divides b evenly
    # increment e until it matches b
    # g winds up zero
    # f set to zero one time if d*e == b, d and f never changed otherwise
    # That means f should be set to 0 if d divides b cleanly (since e goes from 1 to b)

    shouldResetF = False
    if (b % d == 0):
        shouldResetF = True

    return (b, shouldResetF, 0)

debug = False
input1 = 81
input2 = 81
output = 0

if (not debug):
    input1 *= 100
    input1 += 100000
    input2 = input1
    input2 += 17000


output = outestLoop(input1, input2)

print("b: {0}".format(input1))
print("c: {0}".format(input2))
print("h: {0}".format(output))