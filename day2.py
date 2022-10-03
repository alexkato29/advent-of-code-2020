import re

def part1(lines):
    valid = 0

    for line in lines:
        min = int(line[0])
        max = int(line[1])
        target = line[2]
        phrase = line[4]
        count = 0

        for char in phrase:
            if char == target:
                count += 1

        if count >= min and count <= max:
            valid += 1

    return valid


def part2(line):
    valid = 0

    for line in lines:
        pos1 = int(line[0])
        pos2 = int(line[1])
        target = line[2]
        phrase = line[4]

        # Up carot is XOR operator
        if (phrase[pos1 - 1] == target) ^ (phrase[pos2 - 1] == target):
            valid += 1

    return valid


lines = []

# Split with a regex. It could be much better.
with open("inputs/day2.txt", "r") as file:
    for line in file:
        lines.append(re.compile("[ :-]").split(line.strip()))


print(part1(lines))
print(part2(lines))