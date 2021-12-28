x = int (input('xを入力してください:'))
def exp(x):
    n = 1
    genkou = x/n
    exp = 1
    while genkou >= 0.0000001:
        exp += genkou
        n += 1
        genkou *= x/n
    return round(exp, 8)


if x < 0:
    x = -x
    print('1/exp(|x|)=', exp(x))
else:
    print('exp(x)=', exp(x))
