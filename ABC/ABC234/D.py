"""
愚直にやると配列のスライスとソートでO(N^2logN)で無理
最初はP[:K]のmin,次の項が以上の場合はそのまま、小さいなら次に大きいやつ
この操作を繰り返すN-K回
次に大きいやつを高速で見つけたい、元の配列を優先度付きキューでもって最小を消すと次の最小にアクセスできる
これはO(logK),
全体でO(NlogN)で行ける
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC234/input.txt')

N, K = map(int, input().split())
P = list(map(int, input().split()))

import heapq

P_ = []
for i in range(K):
    heapq.heappush(P_, P[i])
p_k = min(P_)
print(p_k)

if N - K >= 1:
    for i in range(K, N):
        #次の項がp_k以下ならK番目に大きいのはp_k
        if P[i] <= p_k:
            p_k = p_k
        #次の項がp_kより大きいなら,最小値を除いて次に小さいやつを見つける
        else:
            heapq.heappush(P_, P[i])
            heapq.heappop(P_) #元p_kを出す
            p_k = P_[0]
        print(p_k)
    

        





