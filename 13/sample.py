
# 基本課題 1. ～ 2. のデータ・ファイル
#
d0 = [ 8, 14, 13, 7, 15, 12, 16, 15, 12, 9 ]

d1 = [ 8, 14, 13, 7, 15 ]

d2 = [ 8, 14, 13, 7, 15, 12, 16, 15, 12, 9, 20, 22, 15, 12, 11,
  25, 13, 7, 10, 6, 11, 11, 5, 8, 16, 7, 11, 18, 12, 9
]

d3 = [
   8, 14, 13, 7, 15, 12, 16, 15, 12, 9, 20, 22, 15, 12, 11,
   8, 14, 13, 7, 15, 12, 16, 15, 12, 9, 20, 22, 15, 12, 11,
  25, 13, 7, 10, 6, 11, 11, 5, 8, 16, 7, 11, 18, 12, 9,
  25, 13, 7, 10, 6, 11, 11, 5, 8, 16, 7, 11, 18, 12, 9,
   8, 14, 13, 7, 15, 12, 16, 15, 12, 9, 20, 22, 15, 12, 11,
  25, 13, 7, 10, 6, 11, 11, 5, 8, 16, 7, 11, 18, 12, 9,
   8, 14, 13, 7, 15, 12, 16, 15, 12, 9, 20, 22, 15, 12, 11,
   8, 14, 13, 7, 15, 12, 16, 15, 12, 9, 20, 22, 15, 12, 11,
  25, 13, 7, 10, 6, 11, 11, 5, 8, 16, 7, 11, 18, 12, 9,
  25, 13, 7, 10, 6, 11, 11, 5, 8, 16, 7, 11, 18, 12, 9
]

d4 = [
  80000, 140000, 130000, 70000, 150000, 120000, 160000, 150000, 120000, 90000, 200000, 220000, 150000, 120000, 110000,
  80000, 140000, 130000, 70000, 150000, 120000, 160000, 150000, 120000, 90000, 200000, 220000, 150000, 120000, 110000,
  250000, 130000, 70000, 100000, 60000, 110000, 110000, 50000, 80000, 160000, 70000, 110000, 180000, 120000, 90000,
  80000, 140000, 130000, 70000, 150000, 120000, 160000, 150000, 120000, 90000, 200000, 220000, 150000, 120000, 110000,
  250000, 130000, 70000, 100000, 60000, 110000, 110000, 50000, 80000, 160000, 70000, 110000, 180000, 120000, 90000,
  250000, 130000, 70000, 100000, 60000, 110000, 110000, 50000, 80000, 160000, 70000, 110000, 180000, 120000, 90000,
  80000, 140000, 130000, 70000, 150000, 120000, 160000, 150000, 120000, 90000, 200000, 220000, 150000, 120000, 110000,
  80000, 140000, 130000, 70000, 150000, 120000, 160000, 150000, 120000, 90000, 200000, 220000, 150000, 120000, 110000,
  250000, 130000, 70000, 100000, 60000, 110000, 110000, 50000, 80000, 160000, 70000, 110000, 180000, 120000, 90000,
  250000, 130000, 70000, 100000, 60000, 110000, 110000, 50000, 80000, 160000, 70000, 110000, 180000, 120000, 90000
]

def puttable(interval, data, n):
    for start in range(len(data)):
        pos = start
        over = 0
        for _ in range(1, n+1):
            d = 0
            while d < interval:
                d += data[pos]
                pos = (pos + 1) % len(data)
                if pos == start:
                    over += 1
        if over == 0 or (over == 1 and pos == start):
            return True
    return False
def main(data:list):
    n = int(input())
    print(f"見張りをする人数: {n}人")
    if n > len(data):
        print('nの値が不正です')
    else:
        total = sum(data)
        l = 0
        h = total
        while l + 1 < h:
            # 二分探索
            m = (1 + h) / 2
            if puttable(m, data, n):
                l = m
            else:
                h = m

        print(f"{n}人を配置するときの塔間の最小値は{l}")
main(d1)
