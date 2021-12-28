import csv

class Student:
    def __init__(self, num:int, name:str, score:int):
        self.num = '{:4d}'.format(int(num))
        self.name = '{:16s}'.format(name)
        self.score = '{:3d}'.format(int(score))


def sorting(array):
    n = len(array)
    for i in range(0, n-1):
        max = i
        for j in range(i+1, n):
            if array[max] < array[j]:
                max = j

        tmp = array[max]
        array[max] = array[i]
        array[i] = tmp


def print_csv(data):
    scores = []
    students = []

    with open(data) as f:
        for row in csv.reader(f):
            num = row[0]
            name = row[1]
            score = row[2]
            student = Student(num, name, score)
            row[0] = student.num
            row[1] = student.name
            row[2] = student.score
            students.append([row[0], row[1], row[2]])
        f.close()

    for i in range(len(students)):
        scores.append(int(students[i][2]))
    sorting(scores)
    for score in scores:
        for i in range(len(students)):
            if score == int(students[i][2]):
                print(students[i])
