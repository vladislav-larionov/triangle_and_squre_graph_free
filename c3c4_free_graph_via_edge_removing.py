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


def remove_triangles(matrix, triangles):
    # print(len(triangles))
    # g[a][b] g[b][c] and g[a][c]:
    a = 0
    b = 1
    c = 2
    for triangle in triangles:
        # print(square)
        weights = {matrix[triangle[a]][triangle[b]]: (triangle[a], triangle[b]),
                   matrix[triangle[b]][triangle[c]]: (triangle[b], triangle[c]),
                   matrix[triangle[a]][triangle[c]]: (triangle[a], triangle[c])}
        m = min(weights.keys())
        indexes = weights[m]
        matrix[indexes[0]][indexes[1]] = 0
        matrix[indexes[1]][indexes[0]] = 0


def remove_squares(matrix, squares):
    # print(len(squares))
    # if g[a][b] and g[a][c] and g[c][d] and g[b][d]:
    a = 0
    b = 1
    c = 2
    d = 3
    for square in squares:
        # print(square)
        weights = {matrix[square[a]][square[b]]: (square[a], square[b]),
                   matrix[square[a]][square[c]]: (square[a], square[c]),
                   matrix[square[c]][square[d]]: (square[c], square[d]),
                   matrix[square[b]][square[d]]: (square[b], square[d])}
        m = min(weights.keys())
        indexes = weights[m]
        matrix[indexes[0]][indexes[1]] = 0
        matrix[indexes[1]][indexes[0]] = 0


def print_result(matrix, edges):
    print(f'c Вес подграфа = {sum(map(lambda e: e[2], edges))}')
    print(f'p edge {len(matrix)} {len(edges)}')
    for e in sorted([f"e {edge_to_str(edge)}\n" for edge in edges]):
        print(e, end='')


if __name__ == "__main__":
    # matrix = read_matrix('../Taxicab_64_matrix_t.txt')
    matrix = read_matrix('D:\Projects\Python\С3C4Free\Taxicab_128_matrix.txt')
    remove_triangles(matrix, find_triangles(matrix))
    remove_squares(matrix, find_squares(matrix))
    # print_result(matrix, matrix_to_edge_list(matrix))
    print_result_matrix(matrix, matrix_to_edge_list(matrix))

    matrix = read_matrix('D:\Projects\Python\С3C4Free\Taxicab_128_matrix.txt')
    remove_squares(matrix, find_squares(matrix))
    remove_triangles(matrix, find_triangles(matrix))
    print_result_matrix(matrix, matrix_to_edge_list(matrix))
