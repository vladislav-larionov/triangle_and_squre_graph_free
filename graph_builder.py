from graph import Graph
from graph_reader import matrix_to_edge_list
from print_utils import print_matrix


def find_graph(graph, n: int, tree=None) -> Graph:
    if not tree:
        tree = Graph(n)
        tree.nodes.add(0)
    edges = set(matrix_to_edge_list(graph))
    for edge in sorted(edges, key=lambda e: e[2], reverse=True):
        if edge[0] in tree.nodes and edge[1] in tree.nodes:
            dist = tree.distance(edge[0], edge[1])
            if dist >= 4 or dist <= 0:
                tree.nodes.add(edge[0])
                tree.nodes.add(edge[1])
                tree.add_edge(edge)
        else:
            tree.nodes.add(edge[0])
            tree.nodes.add(edge[1])
            tree.add_edge(edge)
    return tree


def find_max_edge(edges):
    return max(edges, key=lambda edge: edge[2])


def find_candidates(graph, node, stop_list):
    candidates = set()
    # nearest_nodes = [find_longest_neighbor(graph, stop_list, node)]
    nearest_nodes = find_longest_neighbors(graph, stop_list, node)
    candidates.update((node, nearest_node, graph[node][nearest_node]) for nearest_node in nearest_nodes)
    return candidates


def find_longest_neighbor(graph, tree, node):
    max_dist = 0
    node_index = -1
    for neighbor_i, neighbor_dist in enumerate(graph[node]):
        if neighbor_dist != 0 and neighbor_i not in tree.nodes and neighbor_dist > max_dist:
            max_dist = neighbor_dist
            node_index = neighbor_i
    return node_index


def find_longest_neighbors(graph, stop_list, node) -> list:
    max_dist = 0
    node_indies = []
    for neighbor_i, neighbor_dist in enumerate(graph[node]):
        if neighbor_i not in stop_list and neighbor_dist != 0:
            if neighbor_dist > max_dist:
                max_dist = neighbor_dist
                node_indies.clear()
                node_indies.append(neighbor_i)
            elif neighbor_dist == max_dist:
                node_indies.append(neighbor_i)
    return node_indies
