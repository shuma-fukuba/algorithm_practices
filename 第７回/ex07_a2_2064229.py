# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def bubble_sort(array, start, end):
    for i in range(start, end):
        for j in range(0, end-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# %%
def main():
    array = [1, 8, 43, 2, 5, 7, 2, 123]
    start, end = (int (x) for x in input("開始位置と終了位置?（0, 0が入力されるまで繰り返し）: ").split())
    while start != 0 or end != 0:
        print(f'start: {start}')
        print(f'end: {end}')
        print(bubble_sort(array, start, end))
        start, end = (int (x) for x in input("開始位置と終了位置?（0, 0が入力されるまで繰り返し）: ").split())


# %%
main()


# %%
