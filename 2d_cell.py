#!/usr/bin/python

# A table composed of N x M cells, each having a certain quantity of apples, is
# given. You start from the upper-left corner. At each step you can go down or
# right one cell. Find the maximum number of apples you can collect.


def find_max_weight_path(cell, cur_line, cur_col):
    """Find the path of max weight sum.
    Args:
        cur: a (i,j) tuple representing current location
        cur_sum: cur weight sum
        2d_cell: a N*N 2D array [][] having all the weights, 0<= w_i
    Returns:
        (weight_sum, path) where path is a list of way points
    """
    N = len(cell)
    print("dimension %s, cur line %s, cur col %s" % (N, cur_line, cur_col))

    # Addition
    delta = cell[cur_line][cur_col]
    if cur_line == N-1 and cur_col ==  N-1:
        delta += 0
        return delta

    if cur_line == N-1 and cur_col < N-1:
        delta += find_max_weight_path(cell, cur_line, cur_col+1)
        return delta

    if cur_line < N-1 and cur_col == N-1:
        delta += find_max_weight_path(cell, cur_line+1, cur_col)
        return delta

    if cur_line < N-1 and cur_col < N-1:
        delta += max(find_max_weight_path(cell, cur_line+1, cur_col),
                        find_max_weight_path(cell, cur_line, cur_col+1))
        return delta


if __name__ == "__main__":
    cell = [[0,1,2,3],
            [3,2,1,0],
            [7,0,1,0],
            [0,7,0,1]]
    ret = find_max_weight_path(cell, 0, 0)
    print ret

