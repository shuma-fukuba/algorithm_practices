def factorial(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    return result

n = int(input('nを入力してください'))
print(factorial(n))
