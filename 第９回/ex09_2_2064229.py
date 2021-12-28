perm = []


def solution(n, m=0):
    if n == m:
        print(perm)
    else:
        for x in range(1, n+1):
            if x in perm:
                continue
            perm.append(x)
            solution(n, m+1)
            perm.pop()


def main():
    n = int(input("n = "))
    print("n = ", n)
    if n < 0:
        print("nには正数を入力してください")
    else:
        solution(n)
