# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import itertools


# %%
def thirteen():
    num = [str(n) for n in range(1, 10)]
    for x in itertools.permutations(num):
        left, right = int("".join(x[0:5])), int("".join(x[5:10]))
        a, b = divmod(left, right)
        if a == 13 and b == 0:
            print(f"{left}/{right} = 13")


# %%
thirteen()


# %%
