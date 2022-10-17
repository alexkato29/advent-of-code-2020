import numpy as np


def change_range(low, high, side):
    # side = 0 if we bring lows up, side = 1 if we bring highs down
    diff = (high - low + 1) / 2
    if side == 0:
        low += diff
    else:
        high -= diff
    return low, high


def part1(inputs):
    results = np.array([])

    for string in inputs:
        low_row = 0
        high_row = 127
        low_col = 0
        high_col = 7

        for char in string:
            if char == "F":
                low_row, high_row = change_range(low_row, high_row, 1)
            elif char == "B":
                low_row, high_row = change_range(low_row, high_row, 0)
            elif char == "R":
                low_col, high_col = change_range(low_col, high_col, 0)
            else:
                low_col, high_col = change_range(low_col, high_col, 1)

        results = np.append(results, 8 * low_row + low_col)

    print(np.max(results))
    return results


def part2(values):
    values.sort()
    print(values[0])
    for i in range(int(values[0]), int(values[values.size - 2])):
        if values[i] + 1 != values[i + 1]:
            print(values[i] + 1)
            return values[i] + 1


with open("inputs/day5.txt") as f:
    lines = f.read()

lines = lines.split("\n")
results = part1(lines)
part2(results)
