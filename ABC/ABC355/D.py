"""
共通区間を持つくみの個数を求めたい
共通区間を持てばいいから区間に一括で足し算してそれが２以上になったら共通区間を持つと言える
でもこの方法だと何個重なってるかはわかるけど何組共通しているかはわからない
単純に全部のペアについて判定するとO(N*N)になるから無理
O(N),O(NlogN)のどっちか
重ならない区間のペアを高速で求めて全体から引けばいい
ターゲットのrより相手のlが大きかったら重ならない
ソートして二分探索で境目がわかる、コレはO(NlogN)
"""
#import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC355/input.txt')

import bisect
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
L.sort()
cnt = 0
for i in range(N):
    target_r = R[i]
    border = bisect.bisect_right(L, target_r) 
    cnt += N - border
ans = N * (N - 1) // 2 - cnt
print(ans)


    