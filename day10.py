# Advent of Code 2017, Day 10
# (c) blu3r4y


import numpy as np


def knot_round(nums, lens, pos=0, skip=0):
    for le in lens:
        sel = np.take(nums, np.arange(pos, pos + le), mode='wrap')
        np.put(nums, np.arange(pos + le - 1, pos - 1, step=-1), sel, mode='wrap')
        pos = (pos + le + skip) % len(nums)
        skip += 1

    return nums, pos, skip


def part1(nums, lens):
    nums = knot_round(np.array(nums), np.array(lens))[0]
    return nums[0] * nums[1]


def part2(text):
    lens = np.array([ord(ch) for ch in text] + [17, 31, 73, 47, 23])

    sparse, pos, skip = np.arange(256), 0, 0
    for _ in range(64):
        sparse, pos, skip = knot_round(sparse, lens, pos, skip)

    return ''.join(["%02x" % np.bitwise_xor.reduce(sparse[i:i + 16]) for i in np.arange(0, 256, 16)])


print(part1([0, 1, 2, 3, 4], [3, 4, 1, 5]))
print(part1(range(256), [212, 254, 178, 237, 2, 0, 1, 54, 167, 92, 117, 125, 255, 61, 159, 164]))

print(part2(""))
print(part2("AoC 2017"))
print(part2("1,2,3"))
print(part2("1,2,4"))
print(part2("212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164"))
