"""
一定区間が等差数列
尺取りっぽい気がする
等差数列な間は右を進めて、そうじゃなくなったら左を前に進める
これならO(N)で行ける
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC369/input.txt')

N = int(input())
A = list(map(int, input().split()))

from collections import deque
q = deque()

ans = 0
diff = 0

for a in A:
    q.append(a)
    if len(q) == 3:
        diff = q[1] - q[0]
    #ダメな条件は長さが２より大きく、かつ差が等差でなくなる
    while q and (len(q) > 2 and q[len(q) - 1] - q[len(q) - 2] != diff):
        q.popleft()
    ans += len(q)
print(ans)
