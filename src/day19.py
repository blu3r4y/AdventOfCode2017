# Advent of Code 2017, Day 19
# (c) blu3r4y


import string

import numpy as np
import networkx as nx

MARKERS = ('-', '|', '+')
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def read_graph(file):
    # read the grid
    grid = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            grid.append(np.array(list(line.replace('\n', '').replace('\r', ''))))

    # fix shape
    WIDTH, HEIGHT = len(grid), max([len(e) for e in grid])
    grid = np.array([grid[x][y] if y < len(grid[x]) else ' ' for x in range(WIDTH) for y in range(HEIGHT)])
    grid = grid.reshape((WIDTH, HEIGHT))

    # (c) https://stackoverflow.com/a/1621118
    def neighbors(x, y):
        return [(grid[x + a[0], y + a[1]], x + a[0], y + a[1])
                if ((0 <= x + a[0] < WIDTH) and (0 <= y + a[1] < HEIGHT)) else (' ', None, None)
                for a in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

    # create graph
    g = nx.Graph()
    nodes = [tuple((grid[x, y], x, y)) if grid[x, y] != ' ' else None for x in range(WIDTH) for y in range(HEIGHT)]
    nodes = [node for node in nodes if node is not None]
    g.add_nodes_from(nodes)

    pseudo_id = 0

    # create edges
    az = list(string.ascii_uppercase[:26])
    edges = []
    for node in nodes:
        ne = neighbors(node[1], node[2])
        gi = [grid[n[1], n[2]] if n[1] is not None and n[2] is not None else None for n in ne]

        if node[0] in ['-'] + az:
            if gi[LEFT] in ['-', '+'] + az and gi[RIGHT] in ['-', '+'] + az:
                edges.append((ne[LEFT], node))
                edges.append((node, ne[RIGHT]))
            if node[0] not in az:
                if gi[UP] in ['|'] + az and gi[DOWN] in ['|'] + az:
                    pseudo = ('P%d' % pseudo_id, node[1], node[2])
                    g.add_node(pseudo)
                    edges.append((ne[UP], pseudo))
                    edges.append((pseudo, ne[DOWN]))
                    pseudo_id += 1

        if node[0] in ['|'] + az:
            if gi[UP] in ['|', '+'] + az and gi[DOWN] in ['|', '+'] + az:
                edges.append((ne[UP], node))
                edges.append((node, ne[DOWN]))
            if node[0] not in az:
                if gi[LEFT] in ['-'] + az and gi[RIGHT] in ['-'] + az:
                    pseudo = ('P%d' % pseudo_id, node[1], node[2])
                    g.add_node(pseudo)
                    edges.append((ne[LEFT], pseudo))
                    edges.append((pseudo, ne[RIGHT]))
                    pseudo_id += 1

        if node[0] == '+':
            if gi[UP] in ['|'] + az:
                edges.append((node, ne[UP]))
            if gi[DOWN] in ['|'] + az:
                edges.append((node, ne[DOWN]))
            if gi[LEFT] in ['-'] + az:
                edges.append((node, ne[LEFT]))
            if gi[RIGHT] in ['-'] + az:
                edges.append((node, ne[RIGHT]))

    g.add_edges_from(edges)

    # start node
    start_y = np.argmax([0 if grid[0, y] == ' ' else 1 for y in range(WIDTH)])
    start_node = (grid[0, start_y], 0, start_y)

    return g, start_node


def walk(grid, start_node):
    seq = []
    steps = 0
    node = start_node
    pre_node = node
    while True:
        neigh = list([ne for ne in nx.all_neighbors(grid, node) if ne != pre_node])
        steps += 1
        if len(neigh) == 1:
            pre_node = node
            node = neigh[0]
            if node[0].isalpha():
                seq.append(node[0])
        else:
            break

    return ''.join(seq), steps


def part1(grid, start_node):
    return walk(grid, start_node)[0]


def part2(grid, start_node):
    return walk(grid, start_node)[1]


print(part1(*read_graph('../assets/day19_demo.txt')))
print(part1(*read_graph('../assets/day19.txt')))

print(part2(*read_graph('../assets/day19_demo.txt')))
print(part2(*read_graph('../assets/day19.txt')))
