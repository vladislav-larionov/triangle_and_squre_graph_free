import random
from sys import argv

from graph import Graph, edge_to_str
from graph_reader import read_matrix, matrix_to_edge_list
from graph_rebuilder import rebuild_graph
from print_utils import print_result, print_result_to_file
from spanning_tree import find_spanning_tree
from timer_util import timeit


def find_c3c4_free_graph(graph):
    n = len(graph)
    max_spanning_tree = find_spanning_tree(graph, n)
    # edges = set(matrix_to_edge_list(graph)).difference(max_spanning_tree.edges)
    # for edge in sorted(edges, key=lambda e: e[2], reverse=True):
    #     if max_spanning_tree.distance(edge[0], edge[1]) >= 4:
    #         max_spanning_tree.add_edge(edge)
    old_res = max_spanning_tree.weight
    print(old_res)
    removed = set()
    print_result_to_file(graph, max_spanning_tree)
    for i in range(2):
        max_spanning_tree = rebuild_graph(graph, max_spanning_tree, removed)
        print_result_to_file(graph, max_spanning_tree)
    return max_spanning_tree


@timeit
def main():
    graph = read_matrix(argv[1])
    res = find_c3c4_free_graph(graph)
    print_result(graph, res, short=True)
    print_result_to_file(graph, res, rewrite=False, matrix_print=False)


if __name__ == "__main__":
    main()