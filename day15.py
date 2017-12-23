# Advent of Code 2017, Day 15
# (c) blu3r4y


FA = 16807
FB = 48271
MOD = 2147483647
MASK16 = int('0b' + '1' * 16, 2)


def part1(start_a, start_b, runs, mod_a=1, mod_b=1):
    def generator(val, fact, mod=1):
        while True:
            val = (val * fact) % MOD
            if val % mod == 0:
                yield val & MASK16

    a = generator(start_a, FA, mod=mod_a)
    b = generator(start_b, FB, mod=mod_b)

    result = 0
    for _ in range(runs):
        if next(a) == next(b):
            result += 1
    return result


def part2(start_a, start_b, runs):
    return part1(start_a, start_b, runs, 4, 8)


print(part1(65, 8921, 5))
print(part1(65, 8921, int(40e+6)))
print(part1(116, 299, int(40e+6)))

print(part2(65, 8921, int(5e+6)))
print(part2(116, 299, int(5e+6)))
