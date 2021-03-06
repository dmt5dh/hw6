__author__ = 'Dan'

import sys
import math
import Queue


def a_star(start, finish, grid, wg, wh):
    open_list = Queue.PriorityQueue()
    open_list2 = []
    closed_list = []

    open_list.put(start)
    open_list2.append(start[2])

    while not open_list.empty():
        current_node = open_list.get()
        open_list2.remove(current_node[2])

        if current_node[2] == finish[2]:
            return current_node[1]  # correct return val?

        closed_list.append(current_node[2])
        neighbors_list = get_neighbors(current_node, grid)
        for neighbor in neighbors_list:
            if neighbor[2] in closed_list:
                continue
            given_cost = current_node[1] + 1
            neighbor_coord = neighbor[2]

            if neighbor[2] not in open_list2:
                # print neighbor
                final_cost = (wg * given_cost) + (wh * distance(neighbor, finish))
                neighbor_add = (final_cost, given_cost, neighbor_coord)
                open_list.put(neighbor_add)
                open_list2.append(neighbor_add[2])

    return None


def get_neighbors(current, grid):
    row_limit = len(grid)
    col_limit = len(grid[0])

    neighbors = []
    row_coord = current[2][0]
    col_coord = current[2][1]
    if row_coord + 1 < row_limit and col_coord + 1 < col_limit and row_coord + 1 >= 0 and col_coord + 1 >= 0:
        if grid[row_coord + 1][col_coord + 1] != 'X':
            neighbors.append((0, 0, (row_coord + 1, col_coord + 1)))

    if row_coord - 1 < row_limit and col_coord - 1 < col_limit and row_coord - 1 >= 0 and col_coord - 1 >= 0:
        if grid[row_coord - 1][col_coord - 1] != 'X':
            neighbors.append((0, 0, (row_coord - 1, col_coord - 1)))

    if row_coord + 1 < row_limit and col_coord < col_limit and row_coord + 1 >= 0 and col_coord >= 0:
        if grid[row_coord + 1][col_coord] != 'X':
            neighbors.append((0, 0, (row_coord + 1, col_coord)))

    if row_coord - 1 < row_limit and col_coord < col_limit and row_coord - 1 >= 0 and col_coord >= 0:
        if grid[row_coord - 1][col_coord] != 'X':
            neighbors.append((0, 0, (row_coord - 1, col_coord)))

    if row_coord < row_limit and col_coord + 1 < col_limit and row_coord >= 0 and col_coord + 1 >= 0:
        if grid[row_coord][col_coord + 1] != 'X':
            neighbors.append((0, 0, (row_coord, col_coord + 1)))

    if row_coord < row_limit and col_coord - 1 < col_limit and row_coord >= 0 and col_coord - 1 >= 0:
        if grid[row_coord][col_coord - 1] != 'X':
            neighbors.append((0, 0, (row_coord, col_coord - 1)))

    if row_coord + 1 < row_limit and col_coord - 1 < col_limit and row_coord + 1 >= 0 and col_coord - 1 >= 0:
        if grid[row_coord + 1][col_coord - 1] != 'X':
            neighbors.append((0, 0, (row_coord + 1, col_coord - 1)))

    if row_coord - 1 < row_limit and col_coord + 1 < col_limit and row_coord - 1 >= 0 and col_coord + 1 >= 0:
        if grid[row_coord - 1][col_coord + 1] != 'X':
            neighbors.append((0, 0, (row_coord - 1, col_coord + 1)))

    return neighbors




def distance(a, b):
    x = math.pow((b[2][0] - a[2][0]), 2)
    y = math.pow((b[2][1] - a[2][1]), 2)
    d = math.sqrt(x + y)
    return d


def main(argv):

    fn = str(argv[1])
    f = open(fn, 'r')

    num_cases = int(f.readline())
    while num_cases > 0:
        case_input = f.readline().split()

        grid_width = int(case_input[0])
        grid_height = int(case_input[1])
        wg = float(case_input[2])
        wh = float(case_input[3])

        grid = []  # Every index is a row containing list of columns

        for h in range(0, grid_height):
            row = list(f.readline().split('\n')[0])
            grid.append(row)

        start = (0, 0, (0, 0))
        finish = (0, 0, (0, 0))

        for i in grid:
            for j in i:
                if j == 'S':
                    start = (0, 0, (grid.index(i), i.index(j)))
                if j == 'F':
                    finish = (0, 0, (grid.index(i), i.index(j)))

        dist_sf = distance(start, finish)
        start_cood = start[2]
        start = (dist_sf, 0, start_cood)
        print a_star(start, finish, grid, wg, wh)
        num_cases -= 1


if __name__ == "__main__":
    main(sys.argv)
