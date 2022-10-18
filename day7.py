class Bag:
    def __init__(self, name):
        self.name = name
        self.contents = {}

    def add_bag(self, bag, quantity):
        self.contents[bag] = quantity

    def add_bags(self, bags, quantities):
        for i in range(len(bags)):
            self.add_bag(bags[i], quantities[i])

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        toRet = self.name + ": " + " ".join([val for val in self.contents])
        return toRet


def part1(lines):
    total = 0
    bags = set()
    for rule in lines:
        bag = Bag(rule[0][:-5].strip())
        contents = rule[1].strip()[:-1].split(", ")
        quantities = []
        for i in range(len(contents)):
            quantities.append(contents[i][0])
            if contents[i][0] == 1:
                contents[i] = contents[i][1:-3].strip()
            elif contents[i][0] != "n":
                contents[i] = contents[i][1:-4].strip()
            else:
                contents[i] = ""
        bag.add_bags(contents, quantities)
        bags.add(bag)

    for bag in bags:
        print(bag)
    print(total)
    return total


with open("inputs/day7.txt") as f:
    lines = f.read().split("\n")
    lines = [line.split("contain") for line in lines]

part1(lines)