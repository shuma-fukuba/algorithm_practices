import csv
companion_count = 0
change_count = 0


class Student:
    def __init__(self, num:int, name:str, score:int):
        self.num = '{:4d}'.format(int(num))
        self.name = '{:16s}'.format(name)
        self.score = '{:3d}'.format(int(score))


data1 = 'data_8.csv'
data2 = 'data_288.csv'
data3 = 'data_2240.csv'


def Quicksort(array):
    global companion_count
    global change_count

    n = len(array)

    if n <= 1:
        return array

    pivot = array[0]

    left = []
    right = []

    for i in range(1, n):
        companion_count += 1
        if array[i] >= pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    change_count += 1
    r = Quicksort(right)
    change_count += 1
    l = Quicksort(left)

    return l + [pivot] + r


def main(data, output):
    scores = []
    students = []
    with open(data) as f:
        for row in csv.reader(f):
            student = Student(row[0], row[1], row[2])
            num = student.num
            name = student.name
            score = student.score
            students.append([num, name, score])
            scores.append(int(row[2]))
        f.close()

    scores = Quicksort(scores)
    with open(output, "w") as f:
        for score in scores:
            for student in students:
                if score == int(student[2]):
                    ins_str = student[0] + ',' + student[1] + ',' + student[2] + '\n'
                    f.write(ins_str)

    print('比較回数:', companion_count, ', 入れ替え回数:', change_count)
    print('出力ファイル名:', output)
