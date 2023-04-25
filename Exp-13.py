exp = "a=b*c+b*c"

def solve(exp):
    code = dict((x.split("=")[0], x.split("=")[1]) for x in three(exp))
    finalCode = {}
    for var in code:
        if code[var] not in finalCode:
            finalCode[code[var]] = [var]
        elif code[var] in finalCode:
            finalCode[code[var]].append(var)
    copyVars = {}
    codeList = {}
    for cs,vare in finalCode.items():
        codeList[vare[0]] = cs
        copyVars[vare[0]] = vare[1:]
    for var in copyVars:
        for cv in copyVars[var]:
            for var2,cs in codeList.items():
                codeList[var2] = cs.replace(cv,var)
    return [var+"="+codeList[var] for var in codeList]

def three(exp):
    expressions = []
    reg = ['A','B','C','D','E','F','G','H']
    t = 0
    l = mio(exp)
    while(l!=-1):
        expressions.append(translate(reg[t]+"="+exp[l-1:l+2]))
        exp = exp[:l-1] + reg[t] + exp[l+2:]
        t+=1
        l = mio(exp)
    expressions.append(translate(exp))
    return expressions
        
def translate(exp):
    tr = {
        'A' : 't1',
        'B' : 't2',
        'C' : 't3',
        'D' : 't4',
        'E' : 't5',
        'F' : 't6',
        'G' : 't7',
        'H' : 't8',
    }
    for l in tr:
        exp = exp.replace(l,tr[l])
    return exp

def mio(exp):
    precedence = {
        "*" : 2,
        "/" : 2,
        "+" : 1,
        "-" : 1,
        "" : 0
    }
    lop = ""
    lind = -1
    for ci,c in enumerate(exp):
        if c in precedence and precedence[c] > precedence[lop]:
            lop = c
            lind = ci
    return lind

for s in solve(exp):
    print(s)
