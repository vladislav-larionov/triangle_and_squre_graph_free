import sys

import print_utils
from checkers.connected_components_counter import count_connected_components
from checkers.min_loop_len_finder import find_shortest_cycle_len
from graph_reader import read_matrix


def read_res(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        weight = int(file.readline().split(' ')[-1])
        graph_info = file.readline().split(' ')
        n = int(graph_info[-2])
        e = int(graph_info[-1])
        edges = [list(map(int, line.lstrip('e ').split(' '))) for line in file.readlines()[:e]]
        edges = list(map(lambda e: [e[0]-1, e[1]-1], [edge for edge in edges]))
        print(f'w = {weight}')
        print(f'n = {n}')
        print(f'edges = {e}')
    return edges, weight, n, e


def check_edge_existing(graph, edges, weight):
    total_weight = 0
    for edge in edges:
        total_weight += graph[edge[0]][edge[1]]
    return total_weight == weight


def create_tree_by_edge(graph, edges, n):
    tree = [[0 for i in range(n)] for j in range(n)]
    for edge in edges:
        tree[edge[0]][edge[1]] = graph[edge[0]][edge[1]]
        tree[edge[1]][edge[0]] = graph[edge[1]][edge[0]]
    return tree


def edges_to_node_set(edges):
    nodes = set()
    for e in edges:
        nodes.add(e[0])
        nodes.add(e[1])
    return nodes


def main():
    sys.setrecursionlimit(10000)
    res_file_path = sys.argv[1]
    edges, weight, n, e = read_res(res_file_path)
    graph = read_matrix(f'Taxicab_{n}_matrix.txt')
    print(f'Edges existing: {check_edge_existing(graph, edges, weight)}')
    components = count_connected_components(n, edges)
    print(f'Connected components: {components} {1 == components}')
    shortest_loop = find_shortest_cycle_len(edges, n)
    print(f'Shortest loop: {shortest_loop} {shortest_loop >= 5}')
    if len(sys.argv) > 2:
        with open('checked_matrix.txt', 'w', encoding='utf-8') as f:
            f.write(print_utils.matrix_to_str(create_tree_by_edge(graph, edges, n)))


if __name__ == '__main__':
    main()
