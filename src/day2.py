# Advent of Code 2017, Day 2
# (c) blu3r4y


import numpy as np


def part1(table):
    return np.sum(np.apply_along_axis(lambda row: np.nanmax(row) - np.nanmin(row), 1, table))


def part2(table):
    def search_and_divide(row):
        row = np.sort(row)
        for i, left in enumerate(reversed(row)):
            for right in row[:len(row) - 1 - i]:
                quo, mod = divmod(left, right)
                if mod == 0:
                    return quo

    return np.sum(np.apply_along_axis(search_and_divide, 1, table))


print(part1(np.array([[5, 1, 9, 5], [7, 5, 3, np.nan], [2, 4, 6, 8]])))
print(part1(np.loadtxt('../assets/day2_part1.txt')))

print(part2(np.array([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])))
print(part2(np.loadtxt('../assets/day2_part2.txt')))
