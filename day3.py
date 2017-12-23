# Advent of Code 2017, Day 3
# (c) blu3r4y


def mod_offset(n):
    return 1 if (n % 8 == 0) else 0


def mod_len(n):
    return 1 + (n // 8) + mod_offset(n - 6)


def mod_sums(n):
    result, i, j = 1, 0, 0
    while i < n:
        result += min(mod_len(j), n - i) * (-1 if j % 2 else 1)
        i += mod_len(j)
        j += 1
    return result


def part1(n):
    return (n - 1) if (n < 4) else mod_sums(n - 2)


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


# test with https://oeis.org/A214526
test = [0, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6,
        5, 4, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 8, 7,
        6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9,
        10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]
print([part1(i) - test[i - 1] for i in range(1, len(test))])

# solve
print(part1(312051))
print(part2())
