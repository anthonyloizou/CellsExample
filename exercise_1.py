
cells_1 = [1, 0, 0, 0, 0, 1, 0, 0]

cells_2 = [1, 1, 1, 0, 1, 1, 1, 1]


def get_new_cells_multiple_days(cells, num_of_days):

    if num_of_days == 0:
        return cells
    else:
        new_cells = get_new_cells_one_day(cells)
        new_cells_2 = get_new_cells_multiple_days(new_cells, num_of_days-1)
        return new_cells_2


def get_new_cells_one_day(cells):

    new_cells = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(cells)):

        if i==0:
            if cells[i+1]==1:
                new_cells[i]=1
            else:
                new_cells[i]=0
        elif i==len(cells)-1:
            if cells[i-1]==1:
                new_cells[i]=1
            else:
                new_cells[i]=0
        else:
            if not cells[i-1] == cells[i+1]:
                new_cells[i]=1
            else:
                new_cells[i]=0

    return new_cells


new_cells_one_day_1 = get_new_cells_multiple_days(cells_1, 1)

new_cells_one_day_2 = get_new_cells_multiple_days(cells_2, 2)

print(new_cells_one_day_1)

print(new_cells_one_day_2)
