"""
端からずっと１が連続していれば行かなくいい
より外側に0があるならそこにいく必要がある
スタート地点から見てまずどっちかの端を目指していって一方が完了したらもう一方にいて開閉
そもそもシミュレートする必要なくて端から連続している１の個数を数える、現在の０の個数を数える、間に含まれている１の個数を数える
0の個数＋間に含まれている１の個数＊２
でも初期位置も考慮する必要あるよね
端の１を数えるときは初期位置より右か左かで分けて数え上げる必要がある
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC423/input.txt')

N, R = map(int, input().split())
L = list(map(int, input().split()))

left_1 = 0
right_1 = 0
cnt_0 = 0

#初期位置より左にある端の１
for i in range(R):
    if L[i] == 1:
        left_1 += 1
    else:
        break
##右バージョン
for i in range(N - 1, R - 1, -1):
    if L[i] == 1:
        right_1 += 1
    else:
        break

for i in range(N):
    if L[i] == 0:
        cnt_0 += 1

ans = cnt_0 + 2 * (N - cnt_0 - left_1 - right_1)
print(ans)
