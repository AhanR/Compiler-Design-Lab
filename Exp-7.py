gram = {
	"E":["T*T"],
	"T":["T+T","i"]
}
starting_terminal = "E"

inp = input("Enter the string \n")
inp=inp+"$"

stack = "$"
print("stack\t\t\tbuffer\t\t\taction")
invGrammer = {}
for start in gram:
    for rule in gram[start]:
        invGrammer[rule] = start

while True:
    if stack == "$"+starting_terminal and inp == "$":
        print("String accepted")
        break
    action = ""
    for rule in invGrammer:
        if len(rule)<len(stack) and rule == stack[-len(rule):]:
            action = "Reduce with: "+invGrammer[rule]+"->"+rule
            stack = stack[:-len(rule)] + invGrammer[rule]
            break
    if action[:6] != "Reduce":
        action = "Shift"
        stack+=inp[0]
        inp = inp[1:]
    
    if len(inp) < 1 or action == "":
        print("Reject String")
        break
    print(f"{stack}\t\t\t{inp}\t\t\t{action}")
