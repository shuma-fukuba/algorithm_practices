def mymax(x):
    max = 0
    for i in x:
        if i >= max:
            max = i
    return max


def main():
    x = [1, 2, 3, 5, 7, 90, 77777, 44, 2234, 65, 11]
    print('x[] = ', x)
    print('最大値:', mymax(x))

main()
