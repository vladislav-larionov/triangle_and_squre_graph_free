import dataclasses

from collections import deque


def edge_to_str(edge):
    if edge[0] < edge[1]:
        return str(edge[0]) + " " + str(edge[1])
    else:
        return str(edge[1]) + " " + str(edge[0])


INF = 999999999


@dataclasses.dataclass
class Graph:
    n: int
    nodes: set = dataclasses.field(default_factory=set)
    edges: list = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.adj_matrix = [[0] * self.n for _ in range(self.n)]
        self.adj_list = [set() for _ in range(self.n)]
        self.weight = 0

    def get_leaves(self):
        leaves = []
        for i, v in enumerate(self.adj_list):
            if len(v) == 1:
                leaves.append(i)
        l_edges = []
        for leaf in leaves:
            for i, v in enumerate(self.adj_list):
                if leaf in v:
                    l_edges.append((i, leaf, self.adj_matrix[i][leaf]))
        return l_edges, leaves

    def add_edge(self, edge: tuple):
        self.adj_matrix[edge[0]][edge[1]] = edge[2]
        self.adj_matrix[edge[1]][edge[0]] = edge[2]
        self.edges.append(edge)
        self.adj_list[edge[0]].add(edge[1])
        self.adj_list[edge[1]].add(edge[0])
        self.weight += edge[2]

    def remove_edge(self, edge: tuple):
        self.adj_matrix[edge[0]][edge[1]] = 0
        self.adj_matrix[edge[1]][edge[0]] = 0
        if (edge[1], edge[0], edge[2]) in self.edges:
            self.edges.remove((edge[1], edge[0], edge[2]))
        elif (edge[0], edge[1], edge[2]) in self.edges:
            self.edges.remove((edge[0], edge[1], edge[2]))
        else:
            raise ValueError('There is no such edge')
        self.adj_list[edge[0]].remove(edge[1])
        self.adj_list[edge[1]].remove(edge[0])
        self.weight -= edge[2]

    def remove_edge_by_index(self, index: int):
        edge = self.edges[index]
        self.remove_edge(edge)

    def __repr__(self):
        return f'Tree(nodes={sorted(self.nodes)}, edges={sorted([f"{edge_to_str(edge)} {edge[2]}" for edge in self.edges])})'

    def distance(self, from_node, to_node):
        dist = [0 for i in range(self.n)]
        queue = deque()
        visited = {from_node}
        queue.append(from_node)
        while queue:
            s = queue.popleft()
            for neighbor in self.adj_list[s]:
                if neighbor not in visited:
                    dist[neighbor] = dist[s] + 1
                    if neighbor == to_node:
                        return dist[neighbor]
                    visited.add(neighbor)
                    queue.append(neighbor)
        return dist[to_node]


def bfs_by_matrix(graph, n, node):
    dist = [0 for i in range(n)]
    queue = deque()
    visited = {node}
    queue.append(node)
    while queue:
        s = queue.popleft()
        for neighbor_i, neighbor_dist in enumerate(graph[s]):
            if neighbor_dist != 0 and neighbor_i not in visited:
                dist[neighbor_i] = dist[s] + 1
                visited.add(neighbor_i)
                queue.append(neighbor_i)
    return dist

