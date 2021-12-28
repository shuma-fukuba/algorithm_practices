with open('test1.txt', "w") as f:
    f.write("""
    A - B - C - D - E - F - G
H - I - J - K - L - M - N - O - P
Q - R - S
T - U - V
W - X - Y and Zee
Now I know my A - B - C
Won't you come and sing with me?
    """)
    f.close()


with open('test2.txt', "w") as f:
    f.write("""
    A - B - C - D - E - F - G
H - I - J - K - L - M - N - O - P
Q - R - S
T - U - V
W - X - Y and Zee
Happy, happy, I'm happy
I can sing my ABC
    """)    
    f.close()


def show_file(file):
    with open(file, "r") as f:
        text = f.read()
        f.close()
    return text


def main():
    file1 = input('比較ファイル1:')
    file2 = input('比較ファイル2:')
    text1 = show_file(file1)
    text2 = show_file(file2)
    if text1 == text2:
        print(file1 + 'と' + file2 + 'は内容が同じです')
    else:
        print(file1 + 'と' + file2 + 'は内容が違います')


main()
