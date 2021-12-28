def main():
    lists = []
    while True:
        try:
            val = input("リストに入れる整数を入力してください（終了はEOF）：")
        except EOFError:
            break
        if val:
            lists.append(val)



    for i in range(10):
        count = 0
        for list in lists:
            list = int(list)
            if list == i:
                count += 1
        print(i, 'の個数は', count)


main()
