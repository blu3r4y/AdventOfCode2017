# Advent of Code 2017, Day 5
# (c) blu3r4y


import itertools
import numpy as np


def jump(jumps, strange=False):
    pos = 0
    for step in itertools.count(0):
        try:
            offset = jumps[pos]
            jumps[pos] += 1 if not strange or jumps[pos] < 3 else -1
            pos += offset
        except IndexError:
            return step


def part1(jumps):
    return jump(jumps)


def part2(jumps):
    return jump(jumps, strange=True)


print(part1([0, 3, 0, 1, -3]))
print(part1(np.loadtxt('../assets/day5.txt', dtype=int)))

print(part2([0, 3, 0, 1, -3]))
print(part2(np.loadtxt('../assets/day5.txt', dtype=int)))
