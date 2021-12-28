import csv
import pickle
companion_count = 0
change_count = 0


class Student:
    def __init__(self, num:int, name:str, score:int):
        self.num = '{:4d}'.format(int(num))
        self.name = '{:16s}'.format(name)
        self.score = '{:3d}'.format(int(score))


def sorting(array):
    n = len(array)
    global companion_count
    global change_count
    companion_count = 0
    change_count = 0
    for i in range(0, n-1):
        max = i
        for j in range(i+1, n):
            companion_count += 1
            if array[max] < array[j]:
                max = j
                change_count += 1

        tmp = array[max]
        array[max] = array[i]
        array[i] = tmp


def sorting2(array):
    n = len(array)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j

        tmp = array[min]
        array[min] = array[i]
        array[i] = tmp


def print_csv(data, output_name):
    scores = []
    students = []
    changed_list = []
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
    scores = list(set(scores))
    sorting(scores)

    
    for score in scores:
        score_eqs = []
        nums = []
        for i in range(len(students)):
            if score == int(students[i][2]) and students[i] not in score_eqs:
                score_eqs.append(students[i])
        for eq in score_eqs:
            nums.append(int(eq[0]))
        sorting2(nums)
        for num in nums:
            for eq in score_eqs:
                if int(eq[0]) == num and eq not in changed_list:
                    changed_list.append(eq)


    print('入力ファイル名:', data)
    print('比較回数:', companion_count, ', 入れ替え回数:', change_count)
    with open(output_name, 'w') as f:
        for row in changed_list:
            insert_str = row[0] + ',' + row[1] + ',' + row[2] + '\n'
            f.write(insert_str)
        print(output_name, 'への書き込み完了')
        f.close()
