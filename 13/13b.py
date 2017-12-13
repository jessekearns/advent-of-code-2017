inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\13\\input13.txt"
with open(inputfile) as f:
    lines = f.readlines()
stepsTotal = 0
firewalls = {}
for line in lines:
    segs = line.split(': ')
    firewalls[int(segs[0])]= int(segs[1])
    stepsTotal = int(segs[0])

delay = 0
while True:
    caught = False
    for step in range(0, (stepsTotal + 1)):
        if step in firewalls:
            scannerMod = ((firewalls[step] * 2) - 2)
            if (step + delay) % scannerMod == 0:
                # print ("Delaying {0} steps, I would be caught in layer {1}".format(delay, step))
                caught = True
                break
    if caught:
        delay += 1
    else:
        break

print("\nDelaying {0} steps, I will pass through safely".format(delay))