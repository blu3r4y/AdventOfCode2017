# Advent of Code 2017, Day 17
# (c) blu3r4y


def part1(insertions, steps):
    pos = 0
    buffer = [0]
    for i in range(1, insertions + 1):
        pos = (pos + steps) % len(buffer) + 1
        buffer.insert(pos, i)

    return buffer[(pos + 1) % len(buffer)]


def part2(insertions, steps):
    pos, val = 0, 0
    for i in range(insertions):
        pos = (pos + steps) % (i + 1) + 1
        if pos == 1:
            val = i + 1
    return val


print(part1(2017, 3))
print(part1(2017, 356))

print(part2(2017, 3))
print(part2(50000000, 356))
