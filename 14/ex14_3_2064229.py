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
    def __init__(self, lists):
        self.root = Node(0, None, None)
        for node in lists:
            self.insert(int(node[0]), node[1], node[2])

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

    def search(self, num):
        searcher = self._search_bool(num)
        if searcher is None:
            print('Search target is not found')
        elif searcher is not None:
            print(str(searcher.num) + ' ' + searcher.name + ' ' + searcher.pro)
        elif searcher is None:
            print(str(num) + ' is not found')

    def _search_bool(self, num):
        n = self.root
        if n is None:
            return None
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                if node.num == num:
                    return node
                if node.right is not None:
                    lst.append(node.right)
                if node.left is not None:
                    lst.append(node.left)
            return None

    def del_tree(self, dstt, node):
        if node.right is not None:
            node.right = self.del_tree(dstt, node.right)
        else:
            dstt.num = node.num
            node = node.left
        return node

    def delete(self, num, node):
        if node is None:
            print('{:d} is not found'.format(num))
        elif num < node.num:
            node.left = self.delete(num, node.left)
        elif num > node.num:
            node.right = self.delete(num, node.right)
        else:
            print('{:d} is found. Delete!!'.format(num))
            if node.right is None:
                node = node.left
            elif node.left is None:
                node = node.right
            else:
                node.left = self.del_tree(node, node.left)
        return node


# %%
def file_datas():
    datas = []
    with open('Zac_Japan.txt', encoding='utf-8', mode='r') as f:
            rows = f.readlines()
            for row in rows:
                ret = row.split(' ')
                datas.append(ret)
    return datas


# %%
def main():
    command = 0
    tree = Tree(file_datas())
    while True:
        print('------------------------------------------')
        command = int(input('Menu?(1:探索, 2:表示, 3:削除, 9:終了):'))
        if command == 1:
            num = int(input("検索したい登録番号?: "))
            tree.search(num)
        elif command == 2:
            tree.show(tree.root, 0)
        elif command == 3:
            num = int(input("num = : "))
            tree.delete(num, tree.root)
        elif command == 9:
            print('終了')
            break
        else:
            continue


# %%
main()
