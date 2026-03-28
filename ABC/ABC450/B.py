"""
Cac > Cab + Cbc
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC450/input.txt')

N = int(input())
C = []
for i in range(N - 1):
    row = list(map(int, input().split()))
    C.append([0] * (i + 1) + row)

ans = False

for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            if C[a][c] > C[a][b] + C[b][c]:
                ans = True

if ans:
    print('Yes')
else:
    print('No')