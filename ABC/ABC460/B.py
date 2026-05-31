"""

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC460/input.txt')

T = int(input())
for _ in range(T):
    
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (r1 - r2) ** 2 <=(x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2:
        print('Yes')
    else:
        print('No')
