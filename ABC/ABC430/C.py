"""
条件を満たす文字列の個数→尺取り
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC430/input.txt')

from collections import deque
q = deque()

N, A, B = map(int, input().split())
S = list(input())

cnt_a = 0
cnt_b = 0
ans = 0

for s in S:
    q.append(s)
    if s == 'a':
        cnt_a += 1
    else:
        cnt_b += 1
    #これ以上伸ばしても無理
    while q and cnt_b >= B:
        rm = q.popleft()
        if rm == 'a':
            cnt_a -= 1
        else:
            cnt_b -= 1
    #条件を満たしている場合だけ加える
    if cnt_a >= A:
        ans += 1
print(ans)
    