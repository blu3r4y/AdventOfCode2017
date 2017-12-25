# Advent of Code 2017, Day 25
# (c) blu3r4y


import re
import numpy as np
import pandas as pd
from numba import jit

LEFT, RIGHT = -1, 1


def read_blueprint(file):
    writes = pd.DataFrame(columns=[0, 1])
    moves = pd.DataFrame(columns=[0, 1])
    states = pd.DataFrame(columns=[0, 1])

    with open(file, 'r') as f:
        lines = f.readlines()
        start = ord(re.search('state (?P<state>\w+)', lines[0]).group("state")) - ord('A')
        steps = int(re.search('after (?P<steps>\d+) steps', lines[1]).group("steps"))
        for i in range(3, len(lines), 10):
            state = ord(re.search('state (?P<state>\w+)', lines[i]).group("state")) - ord('A')
            for j in [0, 1]:
                ins_offset = i + 1 + j * 4
                ins_line = ' '.join(lines[ins_offset:ins_offset + 4])
                ins = re.search('value (?P<write>[01]).*?the (?P<move>\w+).*?state (?P<state>\w)', ins_line, re.DOTALL)

                writes.loc[state, j] = ins.group("write")
                moves.loc[state, j] = LEFT if ins.group("move") == "left" else RIGHT
                states.loc[state, j] = ord(ins.group("state")) - ord('A')

        dt = np.int8
        return start, steps, np.array(writes, dtype=dt), np.array(moves, dtype=dt), np.array(states, dtype=dt)


@jit(nopython=True)
def turing(start, steps, writes, moves, states, tape_len=10000):
    offset = tape_len // 2
    tape = np.zeros(tape_len, dtype=np.int8)

    cursor, state = 0, start
    tape[cursor + offset] = 0

    for i in range(steps):
        value = tape[cursor + offset]
        tape[cursor + offset] = writes[state, value]
        cursor += moves[state, value]
        state = states[state, value]

    return np.sum(tape)


def part1(start, steps, writes, moves, states):
    return turing(start, steps, writes, moves, states)


print(part1(*read_blueprint('assets/day25_demo.txt')))
print(part1(*read_blueprint('assets/day25.txt')))
