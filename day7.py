# Advent of Code 2017, Day 7
# (c) blu3r4y


import re
import pandas as pd
import networkx as nx


def read_graph(file):
    g = nx.DiGraph()

    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search('(?P<name>\w+) \((?P<weight>\d+)\)(?: -> (?P<childs>.*))?', line)
            root, weight = match.group("name"), int(match.group("weight"))
            g.add_node(root, weight=weight)
            if match.group("childs") is not None:
                g.add_edges_from([(root, child) for child in match.group("childs").split(', ')])
    return g


def part1(graph):
    # the node with zero in-degree is the root node of a rooted tree
    return [name for name, deg in graph.in_degree() if deg == 0][0]


def part2(graph):
    def _children(node):
        return [(edge[1], graph.nodes[edge[1]]["weight"]) for edge in graph.out_edges(node)]

    def _weights(node, return_tuples=True):
        if return_tuples:
            return [(child[0], sum(_weights(child[0], return_tuples=False)) + child[1]) for child in _children(node)]
        return [sum(_weights(child[0], return_tuples=False)) + child[1] for child in _children(node)]

    current = part1(graph)
    while True:
        weights = pd.DataFrame(_weights(current))
        unique = weights.iloc[:, 1].value_counts()
        if len(unique) == 2:
            # observe the unbalanced child node
            majority_weight = weights.iloc[:, 1].value_counts().idxmax()
            unbalanced_node = weights.loc[weights.iloc[:, 1] != majority_weight, 0]
            unbalanced_child_weights = _weights(unbalanced_node, return_tuples=False)

            if unbalanced_child_weights[1:] == unbalanced_child_weights[:-1]:
                # if the children are balanced, the root node is unbalanced
                return majority_weight - sum(unbalanced_child_weights)
            else:
                # observe the next unbalanced node
                current = unbalanced_node
        else:
            assert len(unique) == 1
            return 0


print(part1(read_graph('assets/day7_demo.txt')))
print(part1(read_graph('assets/day7.txt')))

print(part2(read_graph('assets/day7_demo.txt')))
print(part2(read_graph('assets/day7.txt')))
