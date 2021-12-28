weight = int(input("体重を入力してください:"))
height = int(input("身長を入力してください:"))
gender = int(input("性別（男：1、女：２、男女共用それ以外）を入力してください:"))

if gender == 1:
    n_BMI = 22
elif gender == 2:
    n_BMI = 21
else:
    n_BMI = 21.5

BMI =  weight / ((height / 100) ** 2)
n_weight = (height / 100) ** 2 * n_BMI
obesity = (weight/n_weight -1) * 100

print('BMI:', BMI)
print('標準体重:', n_weight)
print('肥満度:', obesity)

if obesity >= 10:
    print('太り過ぎ')
elif obesity <= -10:
    print('痩せすぎ')
else:
    print('標準')
