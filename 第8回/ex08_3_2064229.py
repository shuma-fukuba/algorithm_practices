def f(n):
    if n == 0:
        return 1
    return n * f(n-1)

def roop(n):
    if n == 0:
        return 1
    else:
        result = 1
        while(n > 1):
            result *= n
            n -= 1
        return result

def main():
    n = int(input('n= '))
    print(f(n))

main()
