def  sqsum( x ):
    result = 0
    for i in range(x+1):
        result += i**2
    return result


x = int(input('n=: '))
print(sqsum(x))
