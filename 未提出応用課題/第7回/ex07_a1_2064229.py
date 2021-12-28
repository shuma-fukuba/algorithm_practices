# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import csv


# %%
class Student:
    def __init__(self, num, name, score):
        self.num = int(num)
        self.name = name
        self.score = score

    def show(self):
        print(f"{str(self.getId()):>4},{self.getName():<16},{str(self.getScore()):>3}")

    def data(self)->list:
        return self.num, self.name, self.score

    def first(self):
        return self.num

    def second(self):
        return self.name

    def third(self):
        return self.score


# %%
def main():
    filename = input("File name?: ")
    with open(filename,"r") as f:
        Students = [Student(Row[0],Row[1],Row[2]) for Row in csv.reader(f)]
        Comp,Swap=0,0


    def merge_sort(array:list, n:int):
        if n <= 1:
            return array
        else:
            midpos = n // 2
            left,right = array[:midpos],array[midpos:]
            return merge(merge_sort(left,len(left)), merge_sort(right,len(right)))


    def merge(left:list, right:list):
        nL,nR = len(left),len(right)
        i,j,Sorted = 0,0,[]
        nonlocal Comp
        nonlocal Swap
        while i < nL and j < nR:
            Comp += 2
            if right[j].third() < left[i].third():
                Sorted.append(left[i]); i += 1
            else:
                Sorted.append(right[j]); j += 1
        while i < nL:
            Swap+=1
            Sorted.append(left[i]); i += 1
        while j < nR:
            Swap+=1
            Sorted.append(right[j]); j += 1
        return Sorted
    sorted_score = merge_sort(Students, len(Students))
    print(f"比較回数: {Comp},入れ替え回数: {Swap}")
    output = input('Output file name?: ')
    with open(output, "w") as f:
        for student in sorted_score:
            csv.writer(f).writerow(student.data())
        print(f"OutputFileName: {output}")


# %%
main()


# %%
main()


# %%
main()


# %%
