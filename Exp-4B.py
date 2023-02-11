rules = {
    'A' : 'aax|aay'
}
nt = ['A']

allLetters = []
for i in range(1,26):
    x = chr(ord("A") + i)
    if x not in nt:
        allLetters.append(x)

def match(s1, s2):
    i = 0
    l = min(len(s1),len(s2))
    while i < l:
        if s1[i] != s2[i]:
            return i
        i+=1
    return i
   
newrules = {}
for rule in rules:
    r = rules[rule].split("|")
   
    m = match(r[0], r[1])
    for prod in r:
        m = min(match(r[0], prod), m)
   
    comn = r[0][:m]
    for i,prod in enumerate(r):
        r[i] = prod[m:]
   
    if(len(comn) > 0):
        newSym = allLetters[0]
        allLetters.pop(0)
        # print(comn)
        newrules[newSym] = comn + rule
    rules[rule] = "|".join(r)

print(rules | newrules)
