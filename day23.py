# Advent of Code 2017, Day 23
# (c) blu3r4y


import cython


@cython.profile(False)
def part1():
    mul = 0
    a, b, c, d, e, f, g, h = 0, 93, 93 + 17, 0, 0, 0, 0, 0

    while b != c:
        f = 1
        mul += (b - 2) * (b - 2)
        for d in range(2, b):
            for e in range(2, b):
                if (d * e) == b:
                    f = 0
        if f == 0:
            h += 1
        b += 17

    return mul


@cython.profile(False)
def factors(n, start=1):
    result = []
    for i in range(start, n // 2 + 1):
        if n % i == 0:
            result.append(i)
    return result


@cython.profile(False)
def part2():
    a, b, c, d, e, f, g, h = 1, 109300, 126300 + 17, 0, 0, 0, 0, 0

    while b != c:
        f = 1
        factor_list = factors(b, start=2)
        for d in factor_list:
            for e in factor_list:
                if (d * e) == b:
                    f = 0
        if f == 0:
            h += 1
        b += 17

    return h


# manually disassembled code in assets/day23.txt
print(part1())
print(part2())
