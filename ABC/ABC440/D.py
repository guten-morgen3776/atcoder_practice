"""
そもそもリスト外の値を答える？？
まずAソートしてxj以上がどこからか知りたい→二分探索
xj以上の要素がkこあるとして、xj+yj+k-1>=max(A)ならmax(A)を超えるのでO(1)で計算できる
そうでない場合はAの間に含まれる、
O(QlogN)で行ける？
その時点でそれ以下にAの要素が何個含まれているかが分かればいいはず
これは事前に計算できる
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC440/input.txt')

import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

#その時点でそれ未満でAの要素でない数が何個含まれているかを事前計算
missing = []
for i in range(N):
    missing.append(A[i] - 1 - i)

for _ in range(Q):
    x, y = map(int, input().split())
    ans = 0
    #二分探索でXの位置を見つける,X未満の要素の個数
    c = bisect.bisect_left(A, x)
    #x以上でy番目にかけている＝全体でx-1-c+y番目
    #missingに対して二分探索して差分を足す
    k = x - 1 - c + y
    miss_idx = bisect.bisect_left(missing, k)
    if miss_idx == 0:
        ans = k
    else:
        ans = A[miss_idx - 1] + k - missing[miss_idx - 1]
    print(ans)


    

        