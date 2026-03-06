"""
r,lがAでどの位置に入るのかを高速で知りたい→二分探索
それまでに何分寝ているかっていう累積和配列を持っておけば求められる？
あとは差分にどれだけ睡眠時間がふくまれているのか
奇数偶数判定はすぐにできるから隙間が睡眠時間かはすぐにわかる
O(NlogN)で行けるはず
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC305/input.txt')

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

#睡眠時間の累積和配列
rui = [0] * (N + 1)
for i in range(2, N + 1):
    if i % 2 == 0:
        rui[i] = rui[i - 1]
    else:
        rui[i] = rui[i - 1] + (A[i - 1] - A[i - 2])

import bisect

for _ in range(Q):
    r, l = map(int, input().split())
    #rの左側、lの右側が知りたい
    r_idx = bisect.bisect_right(A, r) - 1
    l_idx = bisect.bisect_right(A, l) 
    #まずはまとまっている分
    time = rui[l_idx] - rui[r_idx + 2]
    #隙間
    if r_idx % 2 == 1:
        time += A[r_idx + 1] - r
    if l_idx % 2 == 0:
        time += l - A[l_idx - 1]
    print(time)

    


