def calcuration(a, b):
    if a / b == 3:
        print(a, b)

def nodup():
    nums = list(range(1, 10))
    for i in nums:
        for j in nums:
            if i != j:
                for k in nums:
                    if i != k and j != k:
                        for l in nums:
                            if i != l and j != l and k != l:
                                a = int(str(i)+str(j))
                                b = int(str(k)+str(l))
                                calcuration(a, b)
                            else:
                                continue
                    else:
                        continue
            else:
                continue
