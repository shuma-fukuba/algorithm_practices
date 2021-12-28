def Recursion(n, k):
    if k == 0 or k == n:
        return 1
    elif 0 < k:
        Recursion(n-1, k-1)
    else:
        print('0<k<nではありません')


def main():
    print('n, kを入力してください')
    n = int(input('n= '))
    k = int(input('k= '))
    print('n= ', n)
    print('k= ', k)
    print(Recursion(n ,k))
