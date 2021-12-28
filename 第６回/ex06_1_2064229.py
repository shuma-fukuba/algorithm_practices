import csv


class Student:
    def __init__(self, num:int, name:str, score:int):
        self.num = '{:4d}'.format(int(num))
        self.name = '{:16s}'.format(name)
        self.score = '{:3d}'.format(int(score))


data1 = 'data_8.csv'
data2 = 'data_288.csv'
data3 = 'data_2240.csv'


def print_csv(data):
    with open(data) as f:
        for row in csv.reader(f):
            num = row[0]
            name = row[1]
            score = row[2]
            student = Student(num, name, score)
            row[0] = student.num
            row[1] = student.name
            row[2] = student.score
            print(row)
        f.close()




