# Advent of Code 2017, Day 20
# (c) blu3r4y


import numpy as np

P, V, A = 0, 1, 2


def load(file):
    lines = np.loadtxt(file, dtype=str, delimiter=', ')
    vectors = np.array([[[int(e) for e in
                          vec.split('=')[1].strip('<>').split(',')] for vec in
                         line] for line in lines], dtype=float)
    return vectors


def states(t, vectors):
    return [v[P] + t * v[V] + (t * (t + 1) / 2) * v[A] for v in vectors]


def part1(vectors):
    t = 1000
    state = states(t, vectors)
    manhattan = np.argmin([np.sum(abs(v)) for v in state])
    return manhattan


def part2(vectors):
    for t in range(1000):
        state = np.array(states(t, vectors), dtype=np.float64)
        duplicates = [d[0] for d in
                      [np.where((state == un).all(axis=1)) for un in np.unique(state, axis=0)]
                      if len(d[0]) > 1]
        if len(duplicates) > 0:
            duplicates = np.hstack(duplicates)
            vectors = np.delete(vectors, duplicates, axis=0)

    return len(vectors)


print(part1(load('assets/day20_demo1.txt')))
print(part1(load('assets/day20.txt')))

print(part2(load('assets/day20_demo2.txt')))
print(part2(load('assets/day20.txt')))
