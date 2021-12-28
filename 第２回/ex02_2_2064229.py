def twentyfour(n):
    results = []
    for i in range(1, n):
        for j in range(1, n):
            if i * j > 24:
                continue
            if i * j == 24:
                results.append([i, j])

    for i, j in results:
        print(i, j)

twentyfour(9)
