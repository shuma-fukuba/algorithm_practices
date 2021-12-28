def f(n):
    if n <= 1:
        return 1
    else:
        return n * g(n-1)

def g(n):
    if n == 0:
        return 0
    else:
        return n + f(n-1)

def main():
    nums = [0, 1, 4, -10]
    for num in nums:
        print('n = ', num)
        print('f(n) = ', f(num))
        print('g(n) = ', g(num))
        print('\n')
