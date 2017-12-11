def redistributed(banks, i):
    _banks = banks.copy()
    amount = _banks[i]
    _banks[i] = 0
    while amount > 0:
        i = (i + 1) % len(_banks)
        _banks[i] += 1
        amount -= 1
    return _banks

with open("aoc_6_input", "r") as f:
    banks = list()
    for line in f:
        banks = [int(i) for i in line.split()]
    
    configs = list()
    while banks not in configs:
        configs.append(banks)
        banks = redistributed(banks, banks.index(max(banks)))
    print(len(configs))
    print(configs.index(banks))
    print(len(configs)-configs.index(banks))
