class Item:
    def __init__(self, name:str, weight:int):
        self.name = name
        self.weight = weight

items = [Item("A", 7),
        Item("B", 4),
        Item("C", 5),
        Item("D", 6),
        Item("E", 3)]
# 最大積載量
limw = 15
N = len(items)
sel = [False]*N


def try_item(i, tw):
    global sel
    if tw + items[i].weight <= limw:
        sel[i] = True
        if i < N-1:
            try_item(i+1, tw+items[i].weight)

try_item(0, 0)
sel_names = []
print('最大積載量15tの荷物の組み合わせは')
for it, s in zip(items, sel):
    if s:
        sel_names.append(it.name)
print("+".join(sel_names))
