# Advent of Code 2017, Day 24
# (c) blu3r4y


import numpy as np


def all_bridges(puzzle):
    def strengths(bridge, parts, left_right):
        port = bridge[-1][left_right]
        available = [part for part in parts if port in part]
        if len(available) == 0:
            yield len(bridge), np.sum(bridge)
        else:
            for part in available:
                parts_next = parts.copy()
                parts_next.remove(part)
                left_right_next = 1 if port == part[0] else 0
                for length, strength in strengths(bridge + [part], parts_next, left_right_next):
                    yield length, strength

    parts_first = [(0, tuple(puzzle[i])) for i in np.where(0 == puzzle[:, 0])[0]] + \
                  [(1, tuple(puzzle[i])) for i in np.where(0 == puzzle[:, 1])[0]]
    parts = [p for p in map(tuple, puzzle)]

    return [strengths([part], [p for p in parts if p != part], 1 - left_right) for left_right, part in parts_first]


def part1(puzzle):
    return max([max([strength for length, strength in bridges]) for bridges in all_bridges(puzzle)])


def part2(puzzle):
    def longest_bridge(bridges):
        zipped = list(zip(*bridges))
        return max(np.extract(zipped[0] == np.max(zipped[0]), zipped[1]))

    return max([longest_bridge(bridges) for bridges in all_bridges(puzzle)])


print(part1(np.loadtxt('assets/day24_demo.txt', delimiter='/', dtype=int)))
print(part1(np.loadtxt('assets/day24.txt', delimiter='/', dtype=int)))

print(part2(np.loadtxt('assets/day24_demo.txt', delimiter='/', dtype=int)))
print(part2(np.loadtxt('assets/day24.txt', delimiter='/', dtype=int)))
