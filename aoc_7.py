import math


def get_minority(l):
    _max = max(l)
    _min = min(l)
    if l.count(_min) == 1:
        return _max - _min, l.index(_min)
    else:
        return _min - _max, l.index(_max)


class Tree:
    def __init__(self, name, weight, children=None, parent=None):
        if not children:
            children = list()
        self.name = name
        self.children = children
        self.parent = parent
        self.weight = weight

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        print("Appending {} to {}, children are now {}".format(i, self.name, [i.name for i in self.children]))

    def get_weight(self):
        # print(self.name)
        s = 0
        for i in self.children:
            s += i.get_weight()
        return s + self.weight

    def get_unbalanced_node(self, diff=0):
        _diff, child_index = get_minority([c.get_weight() for c in self.children])
        if not self.children or _diff == 0:
            return self.weight + diff, self.name
        return self.children[child_index].get_unbalanced_node(diff=_diff)


def get_node(l, entry):
    for i in l:
        if i.name == entry:
            return i


with open("aoc_7_input", "r") as f:
    support = list()
    for line in f:
        l = line.split()
        d = {"name": l[0], "weight": int(l[1][1:len(l[1])-1]), "leaves": l[3:]}
        support.append(d)
    
    all_nodes = list()
    for d in support:
        all_nodes.append(Tree(d["name"], d["weight"]))

    for d in support:
        node = get_node(all_nodes, d["name"])
        #print("{}: {}".format(d["name"], d["leaves"]))
        for i in d["leaves"]:
            #print("Appending {} to {}".format(i, node.name))
            node.add_child(get_node(all_nodes, i))

    root = [i for i in all_nodes if i.parent is None][0]
    print(root.name)
    print([n.name for n in root.children])
    print(root.get_unbalanced_node())


