

def print_matrix(matrix):
    for row in matrix:
        print(", ".join(map(str, row)))


def matrix_to_str(matrix):
    res = ''
    for row in matrix:
        res += ", ".join(map(str, row)) + '\n'
    return res


def print_result(orig_graph, graph, short=False):
    print(f'c Вес подграфа = {sum(map(lambda e: e[2], graph.edges))}')
    print(f'p edge {len(orig_graph)} {len(graph.edges)}')
    if not short:
        for e in sorted([f"e {edge_to_str(edge)}\n" for edge in graph.edges]):
            print(e, end='')


def print_result_to_file(orig_graph, tree, file_name=None, matrix_print=False, rewrite=False):
    if not file_name:
        file_name = f'temp_res_{tree.n}.txt'
    mode = 'w' if rewrite else 'a+'
    with open(file_name, mode, encoding='utf-8') as file:
        file.write(f'c Вес подграфа = {sum(map(lambda e: e[2], tree.edges))}\n')
        file.write(f'p edge {len(orig_graph)} {len(tree.edges)}\n')
        for e in sorted([f"e {edge_to_str(edge)}\n" for edge in tree.edges]):
            file.write(e)
        file.write("\n")
        if matrix_print:
            file.write(matrix_to_str(tree.adj_matrix))
            file.write("\n")
        file.write("-------------------------------------------")
        file.write("\n")


def edge_to_str(edge):
    if edge[0] < edge[1]:
        return str(edge[0]+1) + " " + str(edge[1]+1)
    else:
        return str(edge[1]+1) + " " + str(edge[0]+1)


def print_formatted_matrix(matrix):
    print('   |\t', end='')
    for i, _ in enumerate(matrix):
        print(f'{i:3}\t', end='')
    print()
    for j, row in enumerate(matrix):
        print(f'{j:3}|\t' + "\t".join([f'{el:3}' for el in row]))


def print_result_matrix(matrix, edges, file_name=None, matrix_print=False, rewrite=False):
    if not file_name:
        file_name = f'temp_res_{len(matrix)}.txt'
    mode = 'w' if rewrite else 'a+'
    with open(file_name, mode, encoding='utf-8') as file:
        file.write(f'c Вес подграфа = {sum(map(lambda e: e[2], edges))}\n')
        file.write(f'p edge {len(matrix)} {len(edges)}\n')
        for e in sorted([f"e {edge_to_str(edge)}\n" for edge in edges]):
            file.write(e)
        file.write("\n")
        if matrix_print:
            file.write(matrix_to_str(matrix))
            file.write("\n")
        file.write("-------------------------------------------")
        file.write("\n")