import time
import pickle

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new

    def display(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next

    def merge_list(self, a, b):
        head = Node(None)
        p = head
        while a and b:
            if a.value <= b.value:
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
        self.head = self.merge_sort_sub(self.head)



l = LinkedList()
with open('Zac_Japan.txt', mode="r", encoding="utf-8") as f:
    for row in f.readlines():
        ret = row.split(' ')
        ret = ret[0]
        l.add(ret)

l.display()
l.merge_sort()
print('#########################')
l.display()
