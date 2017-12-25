# Advent of Code 2017, Day 8
# (c) blu3r4y


import numpy as np


def read(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]


def interpret(instructions):
    variables = np.unique([line.split(' ')[0] for line in instructions])
    exec(', '.join(variables) + " = " + "0, " * (len(variables) - 1) + "0")

    max_eval = "max({})".format(', '.join(variables))
    highest_value = 0

    for instruction in instructions:
        exec(instruction.replace("dec", "-=").replace("inc", "+=") + " else 0")
        if eval(max_eval) > highest_value:
            highest_value = eval(max_eval)

    return eval(max_eval), highest_value


def part1(instructions):
    return interpret(instructions)[0]


def part2(instructions):
    return interpret(instructions)[1]


print(part1(read('assets/day8_demo.txt')))
print(part1(read('assets/day8.txt')))

print(part2(read('assets/day8_demo.txt')))
print(part2(read('assets/day8.txt')))
