"""
max(A)-min(A)を最小にしたい
Aをできるだけ均等にしたい
Aの最小値をできるだけ大きくしたい
常にAの最小値に対して足し続ければいい
最小がどこか把握しておかないといけない
でもそもそも上限回数が設けられてない、どこまで行ったら切り上げる？
modKで考えたらいいのでは？ソートして差分を取って、いやmodとるなら差分取る必要ないか
円環として考えて、区切りを跨がないなら隣との差分をとって最大のもの、跨ぐときは引かれる側+Kしておく
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC450/input.txt')

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [] #modKをとる
for a in A:
    b = a % K
    B.append(b)

B.sort()

ans = float('inf')
if N == 1:
    ans = 0
else:
    max_gap = 0
    for i in range(N - 1):
        if max_gap < B[i + 1] - B[i]:
            max_gap = B[i + 1] - B[i]
    if K + B[0] - B[-1] > max_gap:
        max_gap = K + B[0] - B[-1]
    ans = K - max_gap

print(ans)
        



