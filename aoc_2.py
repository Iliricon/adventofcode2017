with open("aoc_2_input", "r") as f:
    ret_sum = 0
    for line in f:
        loi = [int(i) for i in line.split()]
        for i, x in enumerate(loi):
            for j, y in enumerate(loi):
                if i!=j and (x%y == 0):
                    ret_sum += x/y
                    print(loi)
                    print(x)
                    print(y)
    print(ret_sum)
