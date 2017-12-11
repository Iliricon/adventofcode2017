with open("aoc_11_input", "r") as f:
    distances = list()
    steps = list()
    for l in f:
        steps = l.strip().split(",")
    print(steps)
    pos = [0,0,0]
    for i in steps:
        if i == "s":
            pos[0] -= 1
            pos[2] += 1
        elif i == "se":
            pos[0] -= 1
            pos[1] += 1
        elif i == "sw":
            pos[1] -= 1
            pos[2] += 1
        elif i == "n":
            pos[0] += 1
            pos[2] -= 1
        elif i == "ne":
            pos[1] += 1
            pos[2] -= 1
        elif i == "nw":
            pos[0] += 1
            pos[1] -= 1
        distances.append(sum([abs(i) for i in pos])/2)
    print(pos)
    print(max(distances))
