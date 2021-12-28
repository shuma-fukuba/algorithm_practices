# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Node:
    def __init__(self, num, name, pro, left=None, right=None):
        self.num = int(num)
        self.name = name
        self.pro = pro
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = Node(0, None, None)

    def show(self, node, h:int):
        if node is not None:
            self.show(node.right, h=h+1)
            print("\t"*h, end="")
            print("{:d}".format(node.num), end=" ")
            print(node.name, end=" ")
            print(node.pro)
            self.show(node.left, h=h+1)

    def insert(self, num, name, pro):
        n = self.root
        if n == None:
            self.root = Node(num, name, pro)
            return
        else:
            while True:
                entry = n.num
                if num < entry:
                    if n.left is None:
                        n.left = Node(num, name, pro)
                        return
                    n = n.left
                elif num > entry:
                    if n.right is None:
                        n.right = Node(num, name, pro)
                        return
                    n = n.right
                else:
                    n.num = num
                    return


# %%
def file_datas():
    datas = []
    with open('Zac_japan.txt', encoding='utf-8', mode='r') as f:
            rows = f.readlines()
            for row in rows:
                ret = row.split(' ')
                datas.append(ret)
    return datas


# %%
def main():
    tree = Tree()
    for row in file_datas():
        tree.insert(int(row[0]), row[1], row[2])
    tree.show(tree.root, 0)


# %%
main()


# %%
