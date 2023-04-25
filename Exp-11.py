exp = "a=b*c-a/d"

def solve(exp):
    operatos = ["=","*","+","-","/"]
    tr = {
        "t1": "A" ,
        "t2": "B" ,
        "t3": "C" ,
        "t4": "D" ,
        "t5": "E" ,
        "t6": "F" ,
        "t7": "G" ,
        "t8": "H"
    }
    equations = []
    last = mostImportantOperation(exp)
    t = 1
    while(last != -1):
        equations.append(f"t{t}={translate(exp[last-1:last+2])}")
        exp = exp[:last-1] + tr["t"+str(t)] + exp[last+2:]
        last = mostImportantOperation(exp)
        t+=1
    equations.append(translate(exp))
    return equations
    
def mostImportantOperation(exp):
    precedence = {
        "/" : 2,
        "*" : 2,
        "+" : 1,
        "-" : 1,
        "" : 0
    }
    last = {
        "op" : "",
        "i" : -1
    }
    for ci,c in enumerate(exp):
        if c in precedence and precedence[c] > precedence[last["op"]]:
            last["op"] = c
            last["i"] = ci
    return last["i"]
    
def translate(exp):
    tr = {
        "A" : "t1",
        "B" : "t2",
        "C" : "t3",
        "D" : "t4",
        "E" : "t5",
        "F" : "t6",
        "G" : "t7",
        "H" : "t8",
    }
    for ci,c in enumerate(exp):
        if c in tr:
            exp = exp.replace(c,tr[c])
    return exp
    
    
for stmt in solve(exp):
    print(stmt)
