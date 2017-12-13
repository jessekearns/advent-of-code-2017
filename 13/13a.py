inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\13\\input13.txt"
with open(inputfile) as f:
    lines = f.readlines()
stepsTotal = 0
severity = 0
firewalls = {}
for line in lines:
    segs = line.split(': ')
    firewalls[int(segs[0])]= int(segs[1])
    stepsTotal = int(segs[0])

for step in range(0, stepsTotal + 1):
    if step in firewalls:
        scannerMod = ((firewalls[step] * 2) - 2)
        if step % scannerMod == 0:
            print("Caught in step {0} with depth {1} and severity {2}".format(step, firewalls[step], step*firewalls[step]))
            severity += step*firewalls[step]

print ("\nTotal severity: {0}".format(severity))