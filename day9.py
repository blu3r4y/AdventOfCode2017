# Advent of Code 2017, Day 9
# (c) blu3r4y


import re
import numpy as np


def part1(stream):
    clean = list(re.sub(r"<(!.|.)*?>", "", stream).replace(",", ""))
    level, result = 1, 0
    for ch in clean:
        level += 1 if ch == '{' else -1
        result += level if ch == '}' else 0
    return result


def part2(stream):
    return sum([len(garbage.group(1)) for garbage in re.finditer(re.compile(r"<(.*?)>"), re.sub(r"!.", "", stream))])


print(part1("{}"))
print(part1("{{{}}}"))
print(part1("{{},{}}"))
print(part1("{{{},{},{{}}}}"))
print(part1("{<a>,<a>,<a>,<a>}"))
print(part1("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
print(part1("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
print(part1("{{<a!>},{<a!>},{<a!>},{<ab>}}"))
print(part1(str(np.loadtxt('assets/day9.txt', dtype=str))))

print()
print(part2("<>"))
print(part2("<random characters>"))
print(part2("<<<<>"))
print(part2("<{!>}>"))
print(part2("<!!>"))
print(part2("<!!!>>"))
print(part2('<{o"i!a,<{i<a>'))
print(part2(str(np.loadtxt('assets/day9.txt', dtype=str))))
