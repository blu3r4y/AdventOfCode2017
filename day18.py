# Advent of Code 2017, Day 18
# (c) blu3r4y


from collections import deque
import pandas as pd

INSTRUCTIONS = {'snd': 0, 'set': 1, 'add': 2, 'mul': 3, 'mod': 4, 'rcv': 5, 'jgz': 6}
SND, SET, ADD, MUL, MOD, RCV, JGZ = 0, 1, 2, 3, 4, 5, 6


def preprocess(instructions):
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    instructions['ins'] = instructions['ins'].apply(lambda ins: INSTRUCTIONS[ins])
    for i in [0, 1]:
        instructions['arg%d_int' % i] = instructions['arg%d' % i].apply(
            lambda arg: int(arg) if isinstance(arg, str) and is_int(arg) else 0)
        instructions['arg%d_reg' % i] = instructions['arg%d' % i].apply(
            lambda arg: arg if isinstance(arg, str) and not is_int(arg) else None)
        instructions['arg%d_mode' % i] = instructions['arg%d_reg' % i].apply(lambda arg: 0 if arg is None else 1)
        instructions = instructions.drop(columns=['arg%d' % i])

    return instructions


def interpret(instructions, p=0, pc=0, reg=None, rcv_queue=None, c=0):
    num = len(instructions)
    snd_queue = deque()

    if reg is None:
        reg = dict((key, 0) for key in instructions['arg0_reg'].unique())
        reg['p'] = p

    while pc < num:
        ins = instructions.iloc[pc]
        t = ins['ins']
        a0 = ins['arg0_int'] if ins['arg0_mode'] == 0 else reg[ins['arg0_reg']]
        a1 = ins['arg1_int'] if ins['arg1_mode'] == 0 else reg[ins['arg1_reg']]
        a0_reg = ins['arg0_reg']

        if t == SND:
            snd_queue.append(a0)
            c += 1
        elif t == SET:
            reg[a0_reg] = a1
        elif t == ADD:
            reg[a0_reg] += a1
        elif t == MUL:
            reg[a0_reg] = a0 * a1
        elif t == MOD:
            reg[a0_reg] = a0 % a1
        elif t == RCV:
            if rcv_queue is None:
                if a0 != 0:
                    return snd_queue.pop()
            else:
                try:
                    val = rcv_queue.popleft()
                    reg[a0_reg] = val
                except IndexError:
                    assert len(rcv_queue) == 0
                    return pc, reg, snd_queue, c
        elif t == JGZ:
            if a0 > 0:
                pc = (pc + a1) % num
                continue

        pc += 1

    assert len(rcv_queue) == 0
    return -1, reg, deque(), c


def part1(instructions):
    return interpret(preprocess(instructions))


def part2(instructions):
    instructions = preprocess(instructions)

    c0, c1 = 0, 0
    pc0, pc1 = 0, 0
    reg0, reg1 = None, None
    ppc0, ppc1 = -1, -1
    q0, q1 = deque(), deque()

    while not (pc0 == ppc0 and len(q1) == 0 and pc1 == ppc1 and len(q0) == 0):
        if pc0 >= 0:
            ppc0 = pc0
            pc0, reg0, q0, c0 = interpret(instructions, p=0, pc=pc0, reg=reg0, rcv_queue=q1, c=c0)
        if pc1 >= 0:
            ppc1 = pc1
            pc1, reg1, q1, c1 = interpret(instructions, p=1, pc=pc1, reg=reg1, rcv_queue=q0, c=c1)

    return c0, c1


print(part1(pd.read_csv('assets/day18_demo1.txt', delimiter=' ', names=['ins', 'arg0', 'arg1'])))
print(part1(pd.read_csv('assets/day18.txt', delimiter=' ', names=['ins', 'arg0', 'arg1'])))

print(part2(pd.read_csv('assets/day18_demo2.txt', delimiter=' ', names=['ins', 'arg0', 'arg1'])))
print(part2(pd.read_csv('assets/day18.txt', delimiter=' ', names=['ins', 'arg0', 'arg1'])))
