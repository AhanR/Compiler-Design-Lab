rules = {
    'A' : 'A|e'
}
nt = ['A']

allLetters = []
for i in range(1,26):
    x = chr(ord("A") + i)
    if x not in nt:
        allLetters.append(x)

newrules = {}
for rule in rules:
    r = rules[rule].split("|")
    recProds = []
    oldProds = []
    for prod in r:
        if rule != prod[0]:
            oldProds.append(prod)
        else:
            recProds.append(prod)
   
    for prod in recProds:
        nt.append(allLetters[0])
        newSym = allLetters[0]
        allLetters.pop(0)
        for pi,p in enumerate(oldProds):
            if oldProds[pi] == "e":
                oldProds[pi] = newSym
            else:
                oldProds[pi] += newSym
        newrules[newSym] = prod[1:] + newSym + "|e"
   
    rules[rule] = "|".join(oldProds)

print(rules | newrules)
