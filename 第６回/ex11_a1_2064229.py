# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Student:
    def __init__(self, num:int, name:str, score:int, next=None):
        self.num = int(num)
        self.name = name
        self.score = int(score)
        self.next = next

    def set_score(self, score):
        self.score = score

class Linkedlist:
    def __init__(self):
        self.top = Student(0, None, 0)


    def insert(self, num, name, score):
        front = self.top
        rear = front.next
        while rear and num < rear.num:
            front = rear
            rear = rear.next
        cell = Student(num, name, score)
        cell.next = rear
        front.next = cell

    def show(self):
        p = self.top.next
        while p:
            print('{:4d}'.format(int(p.num)), end=" ")
            print('{:16s}'.format(p.name), end=" ")
            print(p.score)
            p = p.next

    def grade(self):
        p = self.top.next
        while p:
            if int(p.score) >= 90:
                p.set_score('S')
            elif int(p.score) >= 80:
                p.set_score('A')
            elif int(p.score) >= 70:
                p.set_score('B')
            elif int(p.score) >= 60:
                p.set_score('C')
            else:
                p.set_score('F')
            p = p.next
        self.show()


    def writing(self, output):
        p = self.top.next
        with open(output, mode="w", encoding="utf-8") as f:
            while p:
                f.write("{:4d}".format(p.num))
                f.write(' ' + '{:16s}'.format(p.name))
                f.write(str(p.score) + '\n')
                p = p.next


# %%
import csv


# %%
def main(data,output):
    l = Linkedlist()
    with open(data) as f:
        for row in csv.reader(f):
            num = int(row[0])
            name = row[1]
            score = int(row[2])
            l.insert(num, name, score)
    l.grade()

    l.show()
    l.writing(output)


# %%
main('data_8.csv', 'output1.txt')


# %%
main('data_288.csv', 'output2.txt')


# %%
main('data_2240.csv', 'output3.txt')


# %%
