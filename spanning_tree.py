from graph import Graph


def find_spanning_tree(graph, n: int) -> Graph:
    tree = Graph(n)
    tree.nodes.add(0)
    max_edge_count = tree.n - 1
    while len(tree.edges) < max_edge_count:
        candidates = list()
        for node in tree.nodes:
            candidates.extend(find_candidates(graph, node, tree.nodes))
        min_edge = find_max_edge(candidates)
        tree.nodes.add(min_edge[1])
        tree.add_edge((min_edge[0], min_edge[1], min_edge[2]))
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
