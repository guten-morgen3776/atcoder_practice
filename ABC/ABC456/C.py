"""
部分文字列の中で同じ文字が隣り合わないものの個数が知りたい
全探索は無理
尺取りかな？条件を満たすうちは右に伸ばして満たさなくなったら左を上げる
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC456/input.txt')

S = list(input())

from collections import deque
q = deque()

ans = 0

for s in S:
    q.append(s)
    
    while len(q) >= 2 and q[-1] == q[-2]:
        q.popleft()
    
    ans += len(q)
print(ans % 998244353)

