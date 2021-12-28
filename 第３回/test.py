point1 = 0
point2 = 0
def main():

    def tester():
        global point1
        global point2

        point1 += 22
        return point1
    print(tester())

main()
