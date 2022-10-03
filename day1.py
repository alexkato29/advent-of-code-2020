import numpy as np


def find_sum(sorted, target):
    index1 = 0
    index2 = len(sorted) - 1

    for i in range(0, len(sorted)):
        sum = sorted[index1] + sorted[index2]
        if sum > target:
            index2 -= 1
        elif sum < target:
            index1 += 1
        else:
            return sorted[index1], sorted[index2]


with open("inputs/day1.txt", "r") as file:
    nums = np.array([int(line.strip()) for line in file])

nums = np.sort(nums)


def part1():
    """
    Find the two numbers that sum to 2020
    """
    num1, num2 = find_sum(nums, 2020)
    print(num1 * num2)


def part2():
    for num in nums:
        ret = find_sum(nums, 2020 - num)
        if type(ret) == tuple:
            print(num * ret[0] * ret[1])
        break


part1()
part2()
