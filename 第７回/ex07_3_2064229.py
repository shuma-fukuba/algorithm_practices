import csv


class Student:
    def __init__(self, num: int, name: str, score: int):
        self.num = '{:4d}'.format(int(num))
        self.name = '{:16s}'.format(name)
        self.score = '{:3d}'.format(int(score))


data1 = 'data_8.csv'
data2 = 'data_288.csv'
data3 = 'data_2240.csv'


def Quicksort_down(array):
    n = len(array)

    if n <= 1:
        return array

    pivot = array[0]

    left = []
    right = []

    for i in range(1, n):
        if array[i] >= pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    r = Quicksort_down(right)
    l = Quicksort_down(left)

    return l + [pivot] + r


def Quicksort_up(array):
    n = len(array)

    if n <= 1:
        return array

    pivot = array[0]

    left = []
    right = []

    for i in range(1, n):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    r = Quicksort_up(right)
    l = Quicksort_up(left)

    return l + [pivot] + r


def main(data, output):
    scores = []
    students = []
    changed_list = []
    with open(data) as f:
        for row in csv.reader(f):
            student = Student(row[0], row[1], row[2])
            num = student.num
            name = student.name
            score = student.score
            students.append([num, name, score])
            scores.append(int(row[2]))
        f.close()

    scores = list(set(scores))
    scores = Quicksort_down(scores)

    for score in scores:
        score_eqs = []
        nums = []
        for student in students:
            if score == int(student[2]) and student not in score_eqs:
                score_eqs.append(student)
        for eq in score_eqs:
            nums.append(int(eq[0]))

        nums = Quicksort_up(nums)
        for num in nums:
            for eq in score_eqs:
                if int(eq[0]) == num and eq not in changed_list:
                    changed_list.append(eq)

    with open(output, 'w') as f:
        for row in changed_list:
            ins_str = row[0] + ',' + row[1] + ',' + row[2] + '\n'
            f.write(ins_str)
        f.close()
