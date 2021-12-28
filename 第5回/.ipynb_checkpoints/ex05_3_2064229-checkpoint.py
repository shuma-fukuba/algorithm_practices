inverce = []
def inverce(a):
    global inverce
    def det(a):
        return float(a[0][0] * a[1][1] - a[0][1] * a[1][0])
    det = det(a)
    if det != 0:
        z = 1 / det
        inverce =  [[z * a[1][1], z * -a[0][1]], [z * -a[1][0], z * a[0][0]]]
    return det


def main():
    a1 = [0, 0]
    a2 = [0, 0]
    a1[0] = float(input('a[0][0] = '))
    a1[1] = float(input('a[0][1] = '))
    a2[0] = float(input('a[1][0] = '))
    a2[1] = float(input('a[1][1] = '))
    a = [a1, a2]
    print('入力された行列:', a)
    if inverce(a) == 0:
        print('逆行列は存在しません')
    else:
        print('逆行列:', inverce)


main()
