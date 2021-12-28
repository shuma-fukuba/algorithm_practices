count = 0
def fibonacci1(n):
    global count
    count += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n, a=1, b=0):
    global count
    count += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci2(n-1, a+b, a)

def fibonacci3(n):
    global count
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
        count += 1
    return a

def main():
    global count
    n = int(input('n = '))
    if n <= 0:
        print('nは正数ではありません')
    else:
        print('再帰', fibonacci1(n), '呼び出し回数:', count)
        count = 0
        print('末尾再帰', fibonacci2(n, a=1, b=0), '呼び出し回数:', count)
        count = 0
        print('ループ', fibonacci3(n), '繰り返し回数:', count)


main()

