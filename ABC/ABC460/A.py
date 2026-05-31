"""

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC460/input.txt')

N, M = map(int, input().split())

ans = 0
while M > 0:
    x = N % M
    M = x
    ans += 1
print(ans)