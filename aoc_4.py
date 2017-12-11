def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        l1 = list(word1)
        l2 = list(word2)
        for i in l1:
            try:
                l2.remove(i)
            except ValueError:
                pass
        return l2 == []

print(anagram("word1", "1word"))
print(anagram("word1", "word2"))
print(anagram("word10", "word1"))
print(anagram("word1", "ordw1"))

with open("aoc_4_input", "r") as f:
    counter = 0
    for line in f:
        los = line.split()
        line_correct = True
        for i, x in enumerate(los):
            for j, y in enumerate(los):
                if i!=j and anagram(x, y):
                    line_correct = False
                    break
            if not line_correct:
                break
        counter += 1 if line_correct else 0

print(counter)
