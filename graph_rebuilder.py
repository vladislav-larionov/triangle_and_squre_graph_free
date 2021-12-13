import sys

from c3c4_free_graph import rebuild_graph
from checker import read_res
from graph import Graph
from graph_reader import read_matrix
from print_utils import print_result_to_file


def create_tree_by_edge(graph, edges, n):
    tree = Graph(n)
    for edge in edges:
        edge.append(graph[edge[0]][edge[1]])
        tree.nodes.add(edge[0])
        tree.nodes.add(edge[1])
        tree.add_edge(tuple(edge))
    return tree


def main():
    res_file_path = sys.argv[1]
    edges, weight, n, e = read_res(res_file_path)
    matrix = read_matrix(f'Taxicab_{n}_matrix.txt')
    graph = create_tree_by_edge(matrix, edges, n)
    for i in range(2):
        graph = rebuild_graph(matrix, graph)
        print_result_to_file(matrix, graph)


if __name__ == '__main__':
    main()

