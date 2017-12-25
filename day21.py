# Advent of Code 2017, Day 21
# (c) blu3r4y


import itertools
import numpy as np
import cython

GRID = ".#./..#/###"


def load(file):
    def text_to_matrix(text):
        parts = text.split('/')
        mat = np.full((len(parts), len(parts)), False, dtype=bool)
        for x, part in enumerate(parts):
            for y, ch in enumerate(part):
                mat[x, y] = ch == '#'
        return mat

    rules = []
    with open(file, 'r') as f:
        for parts in [line.strip().split(" => ") for line in f]:
            a = text_to_matrix(parts[0])
            b = text_to_matrix(parts[1])
            rules.append([a, b])
            rules.append([np.rot90(a, 1), b])
            rules.append([np.rot90(a, 2), b])
            rules.append([np.rot90(a, 3), b])
            rules.append([np.flip(a, 0), b])
            rules.append([np.flip(np.rot90(a, 1), 0), b])
            rules.append([np.flip(np.rot90(a, 2), 0), b])
            rules.append([np.flip(np.rot90(a, 3), 0), b])

    return text_to_matrix(GRID), rules


@cython.profile(True)
def enhance(mat, rules, iterations):
    for i in range(iterations):
        size = mat.shape[0]
        divisible = 2 if size % 2 == 0 else 3

        factor, factor_new = divisible, divisible + 1
        subsize = size // factor
        size_new = factor_new * subsize

        mat_new = np.full((size_new, size_new), False, dtype=bool)

        for c, e in zip(itertools.product(range(0, size, factor), repeat=2),
                        itertools.product(range(0, size_new, factor_new), repeat=2)):
            submatrix = mat[c[0]:(c[0] + factor), c[1]:(c[1] + factor)]
            found = False
            for rule in rules:
                if np.array_equal(rule[0], submatrix):
                    found = True
                    mat_new[e[0]:(e[0] + factor_new), e[1]:(e[1] + factor_new)] = rule[1]
                    break
            assert found

        mat = mat_new

    return np.sum(mat)


def part1(file, iterations=5):
    return enhance(*load(file), iterations=iterations)


def part2(file):
    return enhance(*load(file), iterations=18)


print(part1('assets/day21_demo.txt', 2))
print(part1('assets/day21.txt'))

print(part2('assets/day21.txt'))
