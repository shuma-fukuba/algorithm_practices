# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def grid_values(grid):
    values = []
    digits = "123456789"
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    grid_int = map(lambda x: int(x) if x != "." else 0, chars)

    count = 0
    row = []
    for i in grid_int:
        row.append(i)
        count += 1
        if count % 9 == 0:
            values.append(row)
            row = []
    return values


# %%
def solver(values, x=0, y=0):
    def check(values, x, y, i):
        def row(values, y, i):
            return all(True if i != values[y][_x] else False for _x in range(9))
        def column(values, x, i):
            return all(True if i != values[_y][x] else False for _y in range(9))
        if row(values, y, i) and column(values, x, i) and block(values, x, y, i):
            return True
        return False

    def block(values, x, y, i):
        xbase = (x // 3) * 3
        ybase = (y // 3) * 3
        return all(True if i != values[_y][_x] else False for _y in range(ybase, xbase + 3) for _x in range(xbase, ybase+3))


    if y > 8:
        return True
    elif values[x][y] != 0:
        if x == 8:
            if solver(values, 0, y+1):
                return True
        else:
            if solver(values, x+1, y):
                return True

    else:
        for i in range(1, 10):
            if check(values, x, y, i):
                values[y][x] = i
                if x == 8:
                    if solver(values, 0,y+1):
                        return True
                else:
                    if solver(values, x+1, y):
                        return True

        values[y][x] = 0
        return False


# %%
grid = """"
8 5 . |. . 2 |4 . .
7 2 . |. . . |. . 9
. . 4 |. . . |. . .
------+------+------
. . . |1 . 7 |. . 2
3 . 5 |. . . |9 . .
. 4 . |. . . |. . .
------+------+------
. . . |. 8 . |. 7 .
. 1 7 |. . . |. . .
. . . |. 3 6 |. 4 .
"""
values = grid_values(grid)


# %%
solver(values)


# %%
for value in values:
    print(value)


# %%
