# Advent of Code 2017, Day 13
# (c) blu3r4y


import itertools
import numpy as np

from numba import jit


@jit(nopython=True)
def severity(ranges, delay=0, fail_fast=False):
    def scanners(t):
        return [-1 if r == 0 else abs(((t - r + 1) % (2 * (r - 1))) - r + 1) for r in ranges]

    sev = 0
    pack = 0
    for t in range(len(ranges)):
        state = scanners(t + delay)
        if pack >= 0 and state[pack] == 0:
            if fail_fast:
                return -1
            sev += t * ranges[t]
        pack += 1

    return sev


def part1(spec):
    ranges = np.zeros(spec[len(spec) - 1, 0] + 1, dtype=int)
    np.put(ranges, spec[:, 0], spec[:, 1])
    return severity(ranges)


def part2(spec):
    ranges = np.zeros(spec[len(spec) - 1, 0] + 1, dtype=int)
    np.put(ranges, spec[:, 0], spec[:, 1])

    for i in itertools.count(0):
        sev = severity(ranges, i, fail_fast=True)
        if sev == 0:
            return i


print(part1(np.array([[0, 3], [1, 2], [4, 4], [6, 4]])))
print(part1(np.loadtxt('../assets/day13.txt', dtype=int, delimiter=':')))

print(part2(np.array([[0, 3], [1, 2], [4, 4], [6, 4]])))
print(part2(np.loadtxt('../assets/day13.txt', dtype=int, delimiter=':')))
