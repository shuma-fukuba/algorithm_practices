def main():
    a = []
    b = []
    n = input("ベクトルの字数（最大10） = ")
    n = int(n)
    print('ベクトル1の入力：')
    for i in range(n):
        ai = input()
        ai = int(ai)
        a.append(ai)
    print('ベクトル2の入力：')
    for i in range(n):
        bi = input()
        bi = int(bi)
        b.append(bi)

    inner_product = 0
    for i in range(0, n):
        inner_product += a[i] * b[i]
    print('内積=', inner_product)

main()
