"""
とりあえずXソート
それぞれの隣接する家との距離を計算して上位M-1個について分割すればいい
それぞれのグループに分けてグループ内の(最大-最小)が電波強度
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC414/input.txt')

N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
#距離を計算、元のインデックスも必要
dis = []
for i in range(1, N):
    dis.append([i, X[i] - X[i - 1]])

#上位M-1この隙間で分割
#距離について降順ソート
dis.sort(reverse=True, key=lambda x: x[1])

ans = 0
if M > 1:
    border = []
    for i in range(M - 1):
        border.append(dis[i][0])
    border.sort()
    ans += X[border[0] - 1] - X[0]
    for i in range(1, M - 1):
        ans += X[border[i] - 1] - X[border[i - 1]] 
    ans += X[-1] - X[border[-1]]
else:
    ans = X[-1] - X[0]

print(ans)




