import math

def main():
    def magnitude(args):
        result = 0
        for i in args:
            result += i ** 2
        result = result **0.5
        return result

    def ip(x, y):
        ip = 0
        for i, j in zip(x, y):
            ip += i * j
        return ip

    def trans(ag):
        return 360 * (ag / (2 * math.pi))

    a0 = int(input('x1=: '))
    a1 = int(input('x2=: '))
    a2 = int(input('x3=: '))
    a = [a0, a1, a2]

    b0 = int(input('y1=: '))
    b1 = int(input('y2=: '))
    b2 = int(input('y3=: '))
    b = [b0, b1, b2]

    mga = round(magnitude(a), 8)
    mgb = round(magnitude(b), 8)
    print(mga)
    print(mgb)
    ip = ip(a, b)

    ag = math.acos(ip/(mga*mgb))
    print(trans(ag))

main()
