# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import random

dgt3 = random.sample(range(10000), k=999)
dgt4 = random.sample(range(100000), k=9999)
dgt5 = random.sample(range(1000000), k=99999)

inputs = [dgt3, dgt4, dgt5]


# %%
def quick(Input):
    comp, swap = 0, 0
    def quick_sub(array, n):
        nonlocal comp
        nonlocal swap

        if n < 1:
            return array
        else:
            piv, left, right = array[0], [], []
            for elem in array[1:]:
                comp += 2
                if elem > piv:
                    swap += 1
                    right.append(elem)

                elif elem < piv:
                    swap += 1
                    left.append(elem)

            left = quick_sub(left, len(left))
            right = quick_sub(right, len(right))
            return left + [piv] + right
    get_ipython().run_line_magic('timeit', '-r 1 -n 1 quick_sub(Input, len(Input))')
    print(f"比較回数: {comp}, 入れ替え回数: {swap}")


# %%
def bubble(Input):
    comp = 0
    swap = 0
    def bubble_sub(array, n):
        nonlocal comp
        nonlocal swap
        for i in range(n):
            for j in range(0, n-i-1):
                comp += 1
                if array[j] > array[j+1]:
                    swap += 1
                    array[j], array[j+1] = array[j+1], array[j]
        return array
    get_ipython().run_line_magic('timeit', '-r 1 -n 1 bubble_sub(Input, len(Input))')
    print(f"比較回数: {comp}, 入れ替え回数: {swap}")


# %%
def select(input):
    def select_sub(array, n):
        comp = 0
        swap = 0
        for i in range(0, n-1):
            min = i
            for j in range(i+1,n):
                comp += 1
                if  array[min] > array[j]:
                    min = j
            swap += 1
            array[min],array[i] = array[i],array[min]
        print(f"比較回数: {comp},入れ替え回数: {swap}")
        return array
    get_ipython().run_line_magic('timeit', '-r 1 -n 1 select_sub(input,len(input))')


# %%
def merge(Input):
    comp = 0
    swap = 0
    def merge_sub(array, n):
        if n <= 1:
            return array
        else:
            center = n // 2
            left, right = array[:center], array[center:]
        def merge_sort(left, right):
            nonlocal comp
            nonlocal swap
            left_l = len(left)
            right_l = len(right)
            i, j, Sorted = 0, 0, []
            while i < left_l and j < right_l:
                if right[j] < left[i]:
                    comp += 1
                    Sorted.append(right[j])
                    j += 1
                else:
                    Sorted.append(left[i])
                    i += 1
            while i < left_l:
                swap += 1
                Sorted.append(left[i])
                i += 1
            while j < right_l:
                swap += 1
                Sorted.append(right[j])
                j += 1
            return Sorted
        return merge_sort(merge_sub(left, len(left)), merge_sub(right, len(right)))
    get_ipython().run_line_magic('timeit', '-r 1 -n 1 merge_sub(Input, len(Input))')
    print(f"比較回数: {comp},入れ替え回数: {swap}")


# %%
for x in inputs:
    quick(x)


# %%
for x in inputs:
    bubble(x)


# %%
for x in inputs:
    merge(x)


# %%
for x in inputs:
    select(x)


# %%
