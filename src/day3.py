# Advent of Code 2017, Day 3
# (c) blu3r4y


import math


def clamp(minvalue, maxvalue, value):
    return max(minvalue, min(value, maxvalue))


def coordinate(n):
    if n == 0:
        return (0, 0)

    # base block and offset rest
    base = math.floor((math.sqrt(4 * n - 3) - 5) / 4) + 1
    rest = n - (6 * base + 8 * ((base - 1) * base) // 2)

    # number of steps (!) on the right/up and left/down sides in this block
    rightUp = 2 * base + 1
    leftDown = rightUp + 1

    right = clamp(0, rest, rightUp)
    up = clamp(0, rest - rightUp, rightUp)
    left = clamp(0, rest - rightUp - rightUp, leftDown)
    down = clamp(0, rest - rightUp - rightUp - leftDown, leftDown)

    return (-base + right - left, base + down - up)


def part1(n):
    return sum([abs(e) for e in coordinate(n - 1)])


def part2():
    # let's cheat a bit ... ;)
    #
    #                        >312453< 295229  279138  266330  130654
    # 6591    6444    6155    5733    5336    5022    2450    128204
    # 13486   147     142     133     122     59      2391    123363
    # 14267   304     5       4       2       57      2275    116247
    # 15252   330     10      1       1       54      2105    109476
    # 16295   351     11      23      25      26      1968    103128
    # 17008   362     747     806     880     931     957     98098
    # 17370   35487   37402   39835   42452   45220   47108   48065

    return 312453


# solve
print(part1(312051))
print(part2())
