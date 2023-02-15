cfg = {}
n = int(input("Enter number of rules: "))
print("Enter rules in the format X->prod1|prod2")
gram = ""
for i in range(n):
    rule = input("Enter rule "+str(i+1)+" : ")
    gram += '\n'+rule
    x = rule.split("->")
    cfg[x[0]] = x[1].split("|")
print("the production is:")
print(gram)

first = {}
for k in cfg:
    first[k] = []

follow = {}
for k in cfg:
    follow[k] = []

# First-----------------------
exploration = []
def ffirst(cfg, rule):
    if rule in exploration:
        return first[rule]
    exploration.append(rule)
    loop = False
    for prod in cfg[rule]:
        if prod[0] in cfg.keys():
            if first[prod[0]] == []:
                y = ffirst(cfg,prod[0])
            elif prod[0] in exploration:
                loop = True
                continue
            else:
                y = first[prod[0]]
            for x in y:
                first[rule].append(x)
        else:
            first[rule].append(prod[0])
    for xi,x in enumerate(exploration):
        if x == rule:
            exploration.pop(xi)
    if loop:
        x = first[rule]
        first[rule] = []
        return x
    return first[rule]

def solveFirst(cfg):
    for k in cfg:
        if first[k] == []:
            ffirst(cfg,k)


#  Follow -------------------------------
def ffollow(cfg, rule):
    for prod in cfg[rule]:
        for ci,c in enumerate(prod):
            if c in cfg.keys():
                if ci+1<len(prod) and prod[ci+1] not in cfg.keys():
                    follow[c].append(prod[ci+1])
                elif ci+1<len(prod) and prod[ci+1] in cfg.keys():
                    for x in first[prod[ci+1]]:
                        follow[c].append(x)
def solveFollow(cfg):
    for rule in cfg:
        ffollow(cfg,rule)

solveFirst(cfg)
solveFollow(cfg)
print("Non-terminals\tfirst\tfollow")
for k in cfg.keys():
    a=",".join(first[k]) if first[k] != [] else "e"
    b=",".join(follow[k]) if follow[k] != [] else "e"
    print(f"{k}\t\t{a}\t{b}")
