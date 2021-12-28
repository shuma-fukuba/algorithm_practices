def data_counter(filename):
    with open('sample1.txt') as f:
        counts = 0
        data = f.read()
        for line in f:
            counts += 1
        f.close()
        print('行数:', counts)

        #単語数のカウント
        for word in data.split():
            counts += 1
        print('単語数:', counts)

        # バイト数のカウント
        counts = 0
        counts = len(data)
        print('バイト数', counts)


def main():
    filename = input('ファイル名を入力してください:')
    data_counter(filename)


main()
