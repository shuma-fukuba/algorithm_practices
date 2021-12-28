class List:
    def __init__(self, num, name, prf, next=None):
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
        self.top = List(0, None, None)

    def index(self):
        num = 1
        while num != 0:
            num = int(input('登録番号？(0で終了)：'))
            n = 0
            cp = self.top
            while cp:
                if cp.first() == num:
                    print(str(cp.first()).rjust(2), end=" ")
                    print(cp.name, end=" ")
                    print(cp.prf)
                    break
                n += 1
                cp = cp.rest()
            if cp == None:
                print('該当者なし')


    def insert(self, num, name, prf):
        front = self.top
        rear = front.next
        while rear and num < rear.num:
            front = rear
            rear = rear.next
        cell = List(num, name, prf)
        cell.next = rear
        front.next = cell

    def delete(self, num):
        front = self.top
        rear = front.next
        while rear:
            if rear.num == num:
                break
            front = rear
            rear = rear.next
        if not rear:
            print("[*]Data not found")
            return
        front.next = rear.next
        rear = None
        print('削除しました')

    def show(self):
        p = self.top.next
        while p:
            print(str(p.num).rjust(2), end=" ")
            print(p.name, end=" ")
            print(p.prf)
            p = p.next

    def merge_list(self, a, b):
        head = List(0, None, None)
        p = head
        while a and b:
            if a.num <= b.num:
                p.next = a
                p = a
                a = a.next
            else:
                p.next = b
                p = b
                b = b.next
        if not a:
            p.next = b
        else:
            p.next = a
        return head.next

    def merge_sort_sub(self, node):
        if not node or not node.next:
            return node
        a = node
        b = node.next
        if b:
            b = b.next
        while b:
            a = a.next
            b = b.next
            if b:
                b = b.next
        p = a.next
        a.next = None
        return self.merge_list(self.merge_sort_sub(node), self.merge_sort_sub(p))

    def merge_sort(self):
        self.top = self.merge_sort_sub(self.top)


l = LinkedList()
file = 'Zac_Japan.txt'
with open(file, mode="r", encoding='UTF-8') as f:
    rows = f.readlines()
    for row in rows:
        ret = row.split(' ')
        l.insert(int(ret[0]), ret[1], ret[2])

l.show()
print('#######並べ替え後#########')
l.merge_sort()
l.show()
