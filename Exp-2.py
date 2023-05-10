re = "ab*c"

state = 0
tfs = []

def solve(re):
    global state
    print("in function")
    # as the regular expression is evaluated left to right keep track of the next incoming processing bit, if no string left to evaluate, exit functuin
    while re != "":
        i = 0
        # look for complicated statements inside block
        if re[0] == "(":
            i+=1
            while re[i]!=")":
                i+=1
            p = re[1:i+1].split("+")
            cs = state
            unclosed=[]
            for pn in p:
                tfs.append(f"d(q{cs},e)->q{state+1}")
                state += 1
                solve(pn)
                unclosed.append(state)

            # close all the states
            for ucs in unclosed:
                tfs.append(f"d(q{ucs},e)->q{state+1}")
            state+=1

            # add in the looping if required
            if i < len(re) and re[i+1] == "*":
                tfs.append(f"d(q{state},e)->q{cs}")
                i+=1
        # add looping on same state for * condition
        elif len(re)>1 and re[1] =="*":
            i+=1
            tfs.append(f"d(q{state},{re[0]})->q{state+1}")
            state+=1
            tfs.append(f"d(q{state},{re[0]})->q{state}")
        # add a new state with a single edge
        else:
            tfs.append(f"d(q{state},{re[0]})->q{state+1}")
            state+=1
        print("completed loop")
        re = re[i+1:]

solve(re)
print(tfs)
