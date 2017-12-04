inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2017\\04\\input4.txt"
with open(inputfile) as f:
    phrases = f.readlines()
total = len(phrases)
valid = 0
invalid = 0
for phrase in phrases:
    cleanphrase = phrase.strip('\n')
    usedwords = []
    thisvalid = True
    for word in cleanphrase.split(' '):
        if word in usedwords:
            thisvalid = False
        usedwords.append(word)
    if thisvalid:
        valid += 1
    else:
        invalid += 1
    
print (valid)
print (invalid)
print (total)