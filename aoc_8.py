instructions = list()
with open("aoc_8_input", "r") as f:
    for line in f:
        x = line.split()
        if x[1] == "inc":
            x[1] = "= " + x[0] + " +" 
        else:
            x[1] = "= " + x[0] + " -"
        instructions.append(x)

registers = set([x[0] for x in instructions])
print("accu = 0")
for i in registers:
    print(i + " = 0")
for i in instructions:
    print(" ".join(i) + " else " + i[0])
    print("if " + i[0] + "> accu:\n\taccu = " + i[0])
#for i in registers:
#    print("print(" + i + ")")
print("print(accu)")
