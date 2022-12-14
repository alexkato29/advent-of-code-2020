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
        for member in group:
            for question in member:
                if question not in seen:
                    seen[question] = 0
                seen[question] += 1
            for key in seen:
                if seen[key] == len(group):
                    sum += 1
    print(sum)
    return sum


with open("inputs/day6.txt") as f:
    lines = f.read().split("\n\n")
    lines2 = [line.split("\n") for line in lines]
    lines = [line.replace("\n", "") for line in lines]

part1(lines)
part2(lines2)
