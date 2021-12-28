def file_read(file):
    with open(file, "r") as f:
        text = f.read()
        f.close()
        print(text)


def file_create(file):
    with open(file, "w") as f:
        f.write("""
a = 3
b = 2
# この行は空行a
x = a / b
print( "a / b == {:f}".format( x ) )
# {:f}はformatメソッドの引数の値を浮動小数点数として解釈する
        """)
        f.close()


def main():
    file = input('ファイル名を入力してください:')
    file_create(file)
    print('コメント抽出前のファイル内容:')
    file_read(file)

    print('コメント抽出後の内容:')
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if len(line) == 0 or line[0] != "#":
                continue
            else:
                print(line)
