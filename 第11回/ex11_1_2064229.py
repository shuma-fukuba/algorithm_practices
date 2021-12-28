class List:
    def __init__(self, num:int, name:str, prf:str, next=None):
        self.num = num
        self.name = name
        self.prf = prf
        self.next = next

    def first(self):
        return self.num

    def rest(self):
        return self.next

    def set_first(self, num):
        self.num = num

    def set_rest(self, x):
        self.next = x


class LinkedList:
    def __init__(self):
        self.top = List(None, None, None)

    def insert(self, num, name, prf):
        front = self.top
        rear = front.next
        while rear and num < rear.num:
            front = rear
            rear = rear.next
        cell = List(num, name, prf)
        cell.next = rear
        front.next = cell

    def show(self):
        p = self.top.next
        while p:
            print(str(p.num).rjust(2), end=" ")
            print(p.name, end=" ")
            print(p.prf)
            p = p.next


def main():
    l = LinkedList()
    file = input("ファイル名を入力:")
    with open(file, mode="r", encoding='UTF-8') as f:
        rows = f.readlines()
        for row in rows:
            ret = row.split(' ')
            l.insert(int(ret[0]), ret[1], ret[2])

    l.show()

main()
