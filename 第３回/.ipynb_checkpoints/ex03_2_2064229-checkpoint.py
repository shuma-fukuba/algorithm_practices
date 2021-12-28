previous = 0
previous_result = 0
def main():
    def sqsum(x):
        result = 0
        global previous
        global previous_result
        if x == previous:
            result = previous_result
        else:
            for i in range(x+1):
                result += i ** 2
            previous = x
            previous_result = sqsum(x)
        return result

    x = 1
    while x >= 0:
        x = int(input('n=: '))
        if previous == x:
            print('previous call')
        print(sqsum(x))

main()
