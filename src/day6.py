# Advent of Code 2017, Day 6
# (c) blu3r4y


import itertools
import numpy as np


def reallocate(banks):
    banks = np.array(banks)
    history = list()

    for step in itertools.count(0):
        selected = int(np.argmax(banks))
        num_blocks = banks[selected]
        banks[selected] = 0

        for i in range(selected + 1, selected + 1 + num_blocks):
            banks[i % len(banks)] += 1

        hashed = hash(banks.data.tobytes())
        if hashed in history:
            cycle_len = [i for i in range(len(history)) if history[i] == hashed][0]
            return step + 1, step - cycle_len
        history.append(hashed)


def part1(banks):
    return reallocate(banks)[0]


def part2(banks):
    return reallocate(banks)[1]


print(part1([0, 2, 7, 0]))
print(part1(np.loadtxt('../assets/day6.txt', dtype=int)))

print(part2([0, 2, 7, 0]))
print(part2(np.loadtxt('../assets/day6.txt', dtype=int)))
