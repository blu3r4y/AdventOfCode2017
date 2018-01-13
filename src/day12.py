# Advent of Code 2017, Day 12
# (c) blu3r4y


import numpy as np
import networkx as nx


def read_graph(spec):
    g = nx.Graph()
    edges = [tuple(e) for e in np.vstack([[(i, j) for j in nd] for i, nd in enumerate(spec)])]
    g.add_nodes_from(range(len(spec)))
    g.add_edges_from(edges)
    return g


def part1(spec):
    g = read_graph(spec)
    return len(nx.node_connected_component(g, 0))


def part2(spec):
    g = read_graph(spec)
    return nx.number_connected_components(g)


print(part1([[int(e) for e in line[1].split(', ')] for line in
             np.loadtxt('../assets/day12_demo.txt', dtype=str, delimiter='<->')]))
print(part1([[int(e) for e in line[1].split(', ')] for line in
             np.loadtxt('../assets/day12.txt', dtype=str, delimiter='<->')]))

print(part2([[int(e) for e in line[1].split(', ')] for line in
             np.loadtxt('../assets/day12_demo.txt', dtype=str, delimiter='<->')]))
print(part2([[int(e) for e in line[1].split(', ')] for line in
             np.loadtxt('../assets/day12.txt', dtype=str, delimiter='<->')]))
