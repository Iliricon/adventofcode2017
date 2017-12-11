with open("aoc_10_input", "r") as f:
    lengths = list()
    for l in f:
        lengths = [int(i) for i in l.split(",")]
    print(lengths)

    sequence = [i for i in range(256)]

    print(sequence)

    current_pos = 0
    skip_length = 0
    for length in lengths:
        end_pos = (current_pos + length) % 256
        sequence[current_pos:end_pos] = reversed(sequence[current_pos:end_pos])
        current_pos += (length + skip_length) % 256
        skip_length += 1
        print(current_pos)
        print(skip_length)
    print(sequence)
