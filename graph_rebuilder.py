import sys

from checker import read_res
from graph import Graph, edge_to_str
from graph_reader import read_matrix, matrix_to_edge_list
from print_utils import print_result_to_file


def create_tree_by_edge(graph, edges, n):
    tree = Graph(n)
    for edge in edges:
        edge.append(graph[edge[0]][edge[1]])
        tree.nodes.add(edge[0])
        tree.nodes.add(edge[1])
        tree.add_edge(tuple(edge))
    return tree


def rebuild_graph(original_graph, graph: Graph, removed: set):
    leaves, leaf_edges = remove_leaves(graph)
    # sorted_leaf_edges = sorted(leaf_edges, key=lambda e: e[2])
    # if len(sorted_leaf_edges) > 5:
    #     sorted_leaf_edges = sorted_leaf_edges[5:]
    for e in list(sorted(graph.edges, key=lambda e: e[2]))[:5]:
         graph.remove_edge(e)
    removed.update([edge_to_str(e) for e in leaf_edges])
    bad_edges = set(removed)
    bad_edges.update([edge_to_str(e) for e in graph.edges])
    bad_edges.update([edge_to_str(e) for e in removed])
    edges = filter(lambda e: edge_to_str(e) not in removed, set(matrix_to_edge_list(original_graph)))
    for edge in sorted(filter(lambda e: e[0] in leaves or e[1] in leaves, edges), key=lambda e: e[2], reverse=True):
        dist = graph.distance(edge[0], edge[1])
        if dist >= 4 or dist <= 1:
            graph.add_edge(edge)
    print(graph.weight)
    return graph


def remove_leaves(graph: Graph):
    leaf_edges, leaves = graph.get_leaves()
    for leaf in leaf_edges:
        graph.remove_edge(leaf)
    return set(leaves), set(leaf_edges)


def main():
    res_file_path = sys.argv[1]
    edges, weight, n, e = read_res(res_file_path)
    matrix = read_matrix(f'Taxicab_{n}_matrix.txt')
    graph = create_tree_by_edge(matrix, edges, n)
    removed = set()
    for i in range(10):
        graph = rebuild_graph(matrix, graph, removed)
        print_result_to_file(matrix, graph)


if __name__ == '__main__':
    main()

