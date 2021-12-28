def key_input():
    mylist = []
    print('文字列を入力してください（入力終了は[ctrl-D]）:')
    while True:
        try:
            val = input()
        except EOFError:
            break
        if val:
                mylist.append(val)

    if mylist:
        print('入力された文字列は以下の通り:')
        for i, item in enumerate(mylist, 1):
            print(i, item)

def main():
    key_input()


main()
