"""

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC459/input.txt')

from collections import defaultdict


N, Q = map(int, input().split())

d = defaultdict(int)
d[0] = N # d[i]: i個以上のブロックを持つますの個数
deleted = 0
blocks = [0] * N
ans = 0

for _ in range(Q):
    x, y = map(int, input().split())
    if x == 1:
        pre_cnt = blocks[y - 1]
        blocks[y - 1] += 1
        d[pre_cnt + 1] += 1
        # 溜まったら消す
        if d[deleted + 1] == N: 
            deleted += 1
    else:
        ans = d[y + deleted] #消した分を考慮
        print(ans)

    