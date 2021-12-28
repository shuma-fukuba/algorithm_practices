with open('Coll_of_ES.txt', "w") as f:
    f.write("""
    Yokohama National University
    College of Engineering Science
    Department of Mathematics, Physics, Electrical Engineering and Computer Science
    """)
    f.close()

with open('Coll_of_ES.txt', "r") as f:
    text = f.read()
    f.close()
    print(text)


def file_copy(source_file, copy_file):
    with open(copy_file, "w") as f1:
        f2 = open(source_file, 'r')
        text = f2.read()
        f2.close()
        f1.write(text)
        f1.close()


def main():
    source_file = input('コピー元のファイル名を入力してください:')
    copy_file = input('コピー先のファイル名を入力してください:')
    file_copy(source_file, copy_file)

main()


with open("copy1.txt", "r") as f:
    text = f.read()
    f.close()
    print(text)
