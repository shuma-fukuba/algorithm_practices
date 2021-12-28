# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def smallcity():
    for i in range(0, pow(3, 9)):
        buf = [0]*9
        for j in reversed(range(9)):
            i, buf[j] = divmod(i, 3)
        operator = []
        if buf[0] == 1:
            operator.append(-9)
        else:
            operator.append(9)

        for j in range(1, 9):
            num = 10- (j + 1)
            if buf[j] == 0:
                op = operator.pop()
                if op > 0:
                    operator.append(10 * op + num)
                else:
                    operator.append(10 * op - num)

            if buf[j] == 1:
                operator.append(-num)
            if buf[j] == 2:
                operator.append(num)

        if sum(operator) == 100 and buf[0] != 2:
            char = {0:"", 1:"-", 2:"+"}
            for i in range(9):
                print(char[buf[i]] + str(9-i), end="")
            print("=100")


# %%
smallcity()


# %%
