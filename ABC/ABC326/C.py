"""
区間内にあるプレゼントの個数を最大化したい
区間和の最大値なので尺取りで実装
区間の幅は決まってるから
区間内の個数、両端を保持しておいてただスライドするだけ
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC326/input.txt')

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

from collections import deque
q = deque()

state = 0
ans = 0

for i in range(N):
    q.append(A[i])
    state += A[i]
    while q and q[-1] - q[0] >= M:
        rm = q.popleft()
        state -= rm
    ans = max(ans, len(q))

print(ans)


