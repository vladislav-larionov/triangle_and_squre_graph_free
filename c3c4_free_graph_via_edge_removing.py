# http://sovietov.com/txt/triangle/triangle.html
from graph_reader import read_graph_as_matrix, read_matrix, matrix_to_edge_list
from print_utils import print_matrix, edge_to_str, matrix_to_str, print_result_matrix


def print_triangles(g):
    n = len(g)
    for a in range(0, n):
        for b in range(a + 1, n):
            if not g[a][b]:
                continue
            for c in range(b + 1, n):
                if g[b][c] and g[a][c]:
                    print(a + 1, b + 1, c + 1)


def print_squares(g):
    n = len(g)
    for a in range(0, n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if g[a][b] and g[a][c] and g[c][d] and g[b][d]:
                        print(a + 1, b + 1, c + 1, d + 1)


def find_triangles(g):
    cycles = []
    n = len(g)
    for a in range(0, n):
        for b in range(a + 1, n):
            if not g[a][b]:
                continue
            for c in range(b + 1, n):
                if g[b][c] and g[a][c]:
                    cycles.append([a, b, c])
    return cycles

"""
Хранить вес квадрата
"""
def find_squares(g):
    cycles = set()
    n = len(g)
    for a in range(0, n):
        for b in range(0, n):
            for c in range(0, n):
                for d in range(0, n):
                    if g[a][b] and g[a][c] and g[c][d] and g[b][d]:
                        if len({a, b, c, d}) == 4:
                            cycles.add((a, b, c, d))
    return cycles


def find_and_remove_triangles(g):
    n = len(g)
    for a in range(0, n):
        for b in range(a + 1, n):
            if not g[a][b]:
                continue
            for c in range(b + 1, n):
                if g[b][c] and g[a][c]:
                    weights = {matrix[a][b]: (a, b),
                               matrix[b][c]: (b, c),
                               matrix[a][c]: (a, c)}
                    m = min(weights.keys())
                    indexes = weights[m]
                    matrix[indexes[0]][indexes[1]] = 0
                    matrix[indexes[1]][indexes[0]] = 0

def find_and_remove_squares(g):
    n = len(g)
    # if g[a][b] and g[a][c] and g[c][d] and g[b][d]:
    for a in range(0, n):
        for b in range(0, n):
            for c in range(0, n):
                for d in range(0, n):
                    if g[a][b] and g[a][c] and g[c][d] and g[b][d]:
                        if len({a, b, c, d}) == 4:
                            weights = {matrix[a][b]: (a, b),
                                       matrix[a][c]: (a, c),
                                       matrix[c][d]: (c, d),
                                       matrix[b][d]: (b, d)}
                            m = min(weights.keys())
                            indexes = weights[m]
                            matrix[indexes[0]][indexes[1]] = 0
                            matrix[indexes[1]][indexes[0]] = 0

def find_and_remove_3c_4c(matrix):
    n = len(matrix)
    for a in range(0, n):
        for b in range(0, n):
            if matrix[a][b] == 0:
                continue
            for c in range(0, n):
                if matrix[a][c] == 0:
                    continue
                if matrix[a][b] and matrix[b][c] and matrix[a][c]:
                    if len({a, b, c}) == 3:
                        weights = {matrix[a][b]: (a, b),
                                   matrix[b][c]: (b, c),
                                   matrix[a][c]: (a, c)}
                        m = min(weights.keys())
                        indexes = weights[m]
                        matrix[indexes[0]][indexes[1]] = 0
                        matrix[indexes[1]][indexes[0]] = 0
                for d in range(0, n):
                    if matrix[a][b] and matrix[a][c] and matrix[c][d] and matrix[b][d]:
                        if len({a, b, c, d}) == 4:
                            weights = {matrix[a][b]: (a, b),
                                       matrix[a][c]: (a, c),
                                       matrix[c][d]: (c, d),
                                       matrix[b][d]: (b, d)}
                            m = min(weights.keys())
                            indexes = weights[m]
                            matrix[indexes[0]][indexes[1]] = 0
                            matrix[indexes[1]][indexes[0]] = 0


def print_result(matrix, edges, short=False):
    print(f'c Вес подграфа = {sum(map(lambda e: e[2], edges))}')
    print(f'p edge {len(matrix)} {len(edges)}')
    if not short:
        for e in sorted([f"e {edge_to_str(edge)}\n" for edge in edges]):
            print(e, end='')


if __name__ == "__main__":
    # matrix = read_matrix('../Taxicab_64_matrix_t.txt')
    matrix = read_matrix('D:\Projects\Python\С3C4Free\Taxicab_4096_matrix.txt')
    find_and_remove_3c_4c(matrix)
    # find_and_remove_squares(matrix)
    print_result(matrix, matrix_to_edge_list(matrix))
    print_result_matrix(matrix, matrix_to_edge_list(matrix))