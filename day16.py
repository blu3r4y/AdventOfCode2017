# Advent of Code 2017, Day 16
# (c) blu3r4y


import numpy as np


def part1(line, moves):
    n = len(line)
    nums = np.array([ord(ch) - ord('a') for ch in line])
    for move in moves:
        t = move[0]

        if t == 's':
            size = int(move[1:])
            nums = nums[np.roll(range(n), size)]
        elif t == 'x':
            a = int(move[1:].split('/')[0])
            b = int(move[1:].split('/')[1])
            nums[a], nums[b] = nums[b], nums[a]
        elif t == 'p':
            a = ord(move[1:].split('/')[0]) - ord('a')
            b = ord(move[1:].split('/')[1]) - ord('a')
            ai = np.where(nums == a)
            bi = np.where(nums == b)
            nums[ai], nums[bi] = nums[bi], nums[ai]

        else:
            raise AssertionError("Invalid move %s" % move)

    return ''.join([chr(i + ord('a')) for i in nums])


def part2(line, moves, repetitions=1000000000):
    history = []
    for i in range(repetitions):
        line = part1(line, moves)
        if line not in history:
            history.append(line)
        else:
            break

    return history[repetitions % len(history) - 1]


print(part1("abcde", ["s1", "x3/4", "pe/b"]))
print(part1("abcdefghijklmnop", np.loadtxt('assets/day16.txt', dtype=str, delimiter=',')))

print(part2("abcde", ["s1", "x3/4", "pe/b"]))
print(part2("abcdefghijklmnop", np.loadtxt('assets/day16.txt', dtype=str, delimiter=',')))
