def part1(groups):
    sum = 0
    for group in groups:
        seen = set()
        for question in group:
            seen.add(question)
        sum += len(seen)
    print(sum)
    return sum


def part2(groups):
    sum = 0
    for group in groups:
        seen = {}


with open("inputs/day6.txt") as f:
    lines = f.read().split("\n\n")
    lines2 = [line.split("\n") for line in lines]
    lines = [line.replace("\n", "") for line in lines]

part1(lines)
part2(lines2)
