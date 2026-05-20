"""
要するにK種類の文字をAから消せる
同じ数字についての和のリストを作ってその上位Kこを消して残りの和を計算すればいい
"""

import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC455/input.txt')

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

sum_ = []
sum_.append(A[0])

for i in range(1, N):
    if A[i - 1] == A[i]:
        sum_[-1] += A[i]
    else:
        sum_.append(A[i])

sum_.sort()

ans = 0
if len(sum_) > K:
    for _ in range(K):
        sum_.pop()
    ans = sum(sum_)

print(ans)

