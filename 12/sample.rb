@d = [
  13, 7, 10, 6, 11, 11, 5, 8, 16, 7, 11, 18, 12, 9,
  14, 13, 7, 15, 12, 16, 15, 12, 9, 20, 22, 15, 12, 11, 8
]

@n = gets.chomp.to_i
@total = @d.inject(:+)

# 指定した間隔を開けて配置できるかチェック
def puttable(interval)
  @d.length.times do |start| # 開始駅
    pos = start
    over = 0 # 1周回った回数
    1.upto(@n) do |i|
      d = 0
      while d < interval do
        d += @d[pos]
        pos = (pos + 1) % @d.length
        over += 1 if pos == start
      end
    end
    # 1周回っていないか、1周回ってちょうど開始駅にいればOK
    return true if (over == 0) || ((over == 1) && (pos == start))
  end
  false
end

l = 0
h = @total

while l + 1 < h do
  # 二分探索
  m = (l + h) / 2
  if puttable(m)
    l = m
  else
    h = m
  end
end

puts l
