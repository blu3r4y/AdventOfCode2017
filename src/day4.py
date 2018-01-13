# Advent of Code 2017, Day 4
# (c) blu3r4y


import pandas as pd
import numpy as np


def part1(passphrases):
    return sum([len(np.unique(phrase)) == len(phrase) for phrase in passphrases])


def part2(passphrases):
    return part1([[sorted(list(word)) for word in phrase] for phrase in passphrases])


print(part1([p.split() for p in pd.read_csv('../assets/day4.txt', header=None).iloc[:, 0]]))
print(part2([p.split() for p in pd.read_csv('../assets/day4.txt', header=None).iloc[:, 0]]))
