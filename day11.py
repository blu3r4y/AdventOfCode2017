# Advent of Code 2017, Day 11
# (c) blu3r4y


import numpy as np

DIRECTIONS = {'n': (0, 1), 'ne': (1, 0), 'se': (1, -1), 's': (0, -1), 'sw': (-1, 0), 'nw': (-1, 1)}
DIRECTIONS = {k: np.array(v) for k, v in DIRECTIONS.items()}


def catch(moves):
    current = np.zeros(2, dtype=int)
    furthest = 0
    for move in [DIRECTIONS[e] for e in moves.split(',')]:
        current += move
        furthest = max(furthest, sum(abs(current)))
    return sum(abs(current)), furthest


def part1(moves):
    return catch(moves)[0]


def part2(moves):
    return catch(moves)[1]


print(part1("ne,ne,ne"))
print(part1("ne,ne,sw,sw"))
print(part1("ne,ne,s,s"))
print(part1("se,sw,se,sw,sw"))
print(part1(str(np.loadtxt('assets/day11.txt', dtype=str))))

print()
print(part2("ne,ne,ne"))
print(part2("ne,ne,sw,sw"))
print(part2("ne,ne,s,s"))
print(part2("se,sw,se,sw,sw"))
print(part2(str(np.loadtxt('assets/day11.txt', dtype=str))))
