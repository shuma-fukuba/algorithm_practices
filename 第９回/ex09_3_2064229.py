op = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while op[0] < 3:
    s = 0
    n = 0
    sign = 1
    for i in range(1, 9):
        if op[i] == 0:
            n = 10*n + i
        else:
            s = s + sign*n
            n = i
            if op[i] == 1:
                sign = 1
            else:
                sign = 1
    s += sign * n
    if s == 100:
        for i in range(1, 9):
            if op[i] == 1:
                print("-")
            else:
                if op[i] == 2:
                    print("+")
            print(i)
        print()
    i = 9
    op[i] = op[i] + 1
    while i > 1 and op[i] == 3:
        op[i] = 0
        i -= 1
        op[i] = op[i]+1
