datas=[
    [8,8,8,8,8,8,8,8,8,8],
    [8,1,0,0,8,8,0,0,0,8],
    [8,0,8,0,0,0,0,8,0,8],
    [8,0,8,8,8,0,8,8,0,8],
    [8,0,0,8,8,0,0,8,0,8],
    [8,8,0,0,8,0,8,8,0,8],
    [8,0,8,0,8,0,0,8,0,8],
    [8,0,0,0,8,8,0,0,0,8],
    [8,8,8,0,0,0,0,8,0,8],
    [8,8,8,8,8,8,8,8,9,8]
]


def printmaps(datas):
    for data in datas:
        for i in data:
            if i == 0:
                print(" ", end=" ")
            elif i == 1 or i == 9:
                print("○", end=" ")
            elif i == 8:
                print("■", end=" ")
        print()

printmaps(datas)
