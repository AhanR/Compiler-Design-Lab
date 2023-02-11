nfa = {
    '0' : { '0' : '0', '1' : ['1','2'] },
    '1' : { '0' : '1' },
    '2' : { '0' : '2' },
}

def convert(nfa):
    dfa = {}
    newStates = []
    for s in nfa:
        dfa[s] = {}
        n = 0
        for t in nfa[s]:
            out = nfa[s][t]
            if len(out) > 1:
                out = "".join(out)
                if out not in newStates:
                    newStates.append(out)
            dfa[s][t] = out
    
    while len(newStates) > 0:
        tempNewStates = []
        for ns in newStates:
            dfa[ns] = {}
            for c in ns:
                for t in dfa[c]:
                    if t in dfa[ns].keys():
                        out = dfa[ns][t] + dfa[c][t]
                        dfa[ns][t] = out
                        if out not in newStates and out not in dfa.keys():
                            tempNewStates.append(out)
                    else:
                        dfa[ns][t] = dfa[c][t]
        newStates = tempNewStates
                
    
    return dfa

print(convert(nfa))
