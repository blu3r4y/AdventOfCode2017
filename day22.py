# Advent of Code 2017, Day 22
# (c) blu3r4y


import numpy as np
from collections import defaultdict

# up, left, down, right
DIRECTIONS = np.array([[-1, 0], [0, -1], [1, 0], [0, 1]])
FACE_LEFT, FACE_RIGHT, FACE_REVERSE, FACE_NONE = 1, -1, 2, 0

# cell states
CLEAN, WEAKENED, INFECTED, FLAGGED = 0, 1, 2, 3
FACE_DECISIONS = [FACE_LEFT, FACE_NONE, FACE_RIGHT, FACE_REVERSE]


def read_matrix(file):
    mat = defaultdict(int)
    with open(file, 'r') as f:
        lines = f.readlines()
        center_offset = len(lines) // 2
        for x, line in enumerate(lines):
            for y, ch in enumerate(line):
                mat[x - center_offset, y - center_offset] = INFECTED if ch == '#' else CLEAN

    return mat


def simulate(mat, bursts, advanced=False):
    current = np.array([0, 0])
    direction = 0
    num_infections = 0
    for i in range(bursts):
        cell = mat[current[0], current[1]]
        direction = (direction + FACE_DECISIONS[cell]) % len(DIRECTIONS)
        cell_new = (cell + 1) % 4 if advanced else (CLEAN if cell == INFECTED else INFECTED)
        mat[current[0], current[1]] = cell_new
        if cell_new == INFECTED:
            num_infections += 1
        current += DIRECTIONS[direction]

    return num_infections


def part1(mat, bursts):
    return simulate(mat, bursts)


def part2(mat, bursts):
    return simulate(mat, bursts, True)


print(part1(read_matrix('assets/day22_demo.txt'), 7))
print(part1(read_matrix('assets/day22_demo.txt'), 70))
print(part1(read_matrix('assets/day22_demo.txt'), 10000))
print(part1(read_matrix('assets/day22.txt'), 10000))

print()
print(part2(read_matrix('assets/day22_demo.txt'), 100))
print(part2(read_matrix('assets/day22_demo.txt'), 10000000))
print(part2(read_matrix('assets/day22.txt'), 10000000))
