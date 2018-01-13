# Advent of Code 2017, Day 14
# (c) blu3r4y


import numpy as np

X, Y = 128, 128


def knot_hash(text):
    """
    Advent of Code 2017, Day 10
    """

    def knot_round(nums, lens, pos=0, skip=0):
        for le in lens:
            sel = np.take(nums, np.arange(pos, pos + le), mode='wrap')
            np.put(nums, np.arange(pos + le - 1, pos - 1, step=-1), sel, mode='wrap')
            pos = (pos + le + skip) % len(nums)
            skip += 1

        return nums, pos, skip

    lens = np.array([ord(ch) for ch in text] + [17, 31, 73, 47, 23])
    sparse, pos, skip = np.arange(256), 0, 0
    for _ in range(64):
        sparse, pos, skip = knot_round(sparse, lens, pos, skip)

    return np.array([np.bitwise_xor.reduce(sparse[i:i + 16]) for i in np.arange(0, 256, 16)], dtype=np.uint8)


# (c) https://stackoverflow.com/a/1621118
def neighbors(x, y):
    return [(x + a[0], y + a[1]) for a in
            [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if ((0 <= x + a[0] < X) and (0 <= y + a[1] < Y))]


def part1(key):
    return np.sum([np.sum(np.unpackbits(knot_hash("%s-%d" % (key, i)))) for i in range(Y)])


def part2(key):
    grid = np.array([np.unpackbits(knot_hash("%s-%d" % (key, i))) for i in range(128)])
    regions, marked = np.zeros_like(grid), np.zeros_like(grid)

    def flood_fill(x, y, region=0):
        # already observed
        if marked[x, y] == 1:
            return False
        marked[x, y] = 1

        # fill cell and observe neighbors
        if grid[x, y] == 1:
            regions[x, y] = region
            for nx, ny in neighbors(x, y):
                if marked[nx, ny] == 0:
                    flood_fill(nx, ny, region)
            return True

        return False

    def find_regions():
        region = 1
        for x in range(X):
            for y in range(Y):
                if flood_fill(x, y, region):
                    region += 1
        return region - 1

    return find_regions()


print(part1("flqrgnkx"))
print(part1("ugkiagan"))

print(part2("flqrgnkx"))
print(part2("ugkiagan"))
