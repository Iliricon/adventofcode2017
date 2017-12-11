with open ("aoc_9_input", "r") as f:
    stream = list()
    for line in f:
        stream = list(line)
    print(stream)

    score = 0
    accumulator = 0
    in_garbage = False
    i = 0
    garbage_counter = 0

    while i < len(stream):
        if stream[i] == "!":
            i += 1
        elif in_garbage:
            if stream[i] == ">":
                in_garbage = False
            else:
                garbage_counter += 1
        elif not in_garbage:
            if stream[i] == "{":
                score = score + 1
            if stream[i] == "}":
                accumulator += score
                score = score - 1
            if stream[i] == "<":
                in_garbage = True
        i += 1

    print(accumulator)
    print(score)
    print(garbage_counter)

