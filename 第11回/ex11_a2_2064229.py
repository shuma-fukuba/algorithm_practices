# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Node:
    def __init__(self, word):
        self.word = word
        self.next = None
    def first(self):
        return self.word
    def rest(self):
        return self.next
    def set_first(self, word):
        self.word = word
    def set_rest(self, x):
        self.next = x

# %% [markdown]
#

# %%
class LinkedList:
    def __init__(self):
        self.top = Node(None)

    def show(self):
        p = self.top.next
        while p:
            print(p.first())
            p = p.rest()

    def delete(self, word):
        front = self.top
        rear = front.next
        while rear:
            if rear.word == word:
                break
            front = rear
            rear = rear.next
        if not rear:
            return
        front.next = rear.next
        rear = None

    def insert(self, name):
        front = self.top
        rear = front.rest()
        while rear:
            front = rear
            rear = rear.next
        cell = Node(name)
        cell.next = rear
        front.next = cell

    def linkedsearch(self):
        top = self.top.next
        while top:
            rear = self.top.next
            count = 0
            while rear:
                if top.word == rear.word:
                    count += 1
                rear = rear.next
            print(top.word, end=": ")
            print(count)
            top = top.next

    def halfSearch(self):
        def sorting():
            top = self.top.next
            rest = []
            while top:
                rest.append(top.word)
                self.delete(top.word)
                top = top.next
            rest = sorted(rest)
            top = self.top
            for x in rest:
                self.insert(x)
        sorting()
        top = self.top.next
        while top:
            count = 1
            rear = top.next
            while rear:
                if top.word == rear.word:
                    count += 1
                rear = rear.next
            print(top.word, end=": ")
            print(count)
            top = top.next


# %%
def main(filename):
    l = LinkedList()
    with open(filename, mode="r", encoding="utf-8") as f:
        rows = f.read()
        rows = rows.replace(',', ' ')
        rows = rows.replace('\n', ' ')
        ret = rows.split(' ')
        count = 0
        ret2 = []
        while count < len(ret):
            if ret[count] != '':
                ret2.append(ret[count])
            count += 1

    for x in ret2:
        l.insert(x)

    print('##########線形探索#############')
    l.linkedsearch()
    print('##########二分探索#############')
    l.halfSearch()


# %%
main('Coll_of_ES.txt')


# %%
main('Coll_of_ES_EPs.txt')


# %%
main('Dep_of_M-P-EE-CS.txt')


# %%
