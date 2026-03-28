"""

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC451/input.txt')

N, M = map(int, input().split())
team_1 = [0] * M
team_2 = [0] * M
for _ in range(N):
    a, b = map(int, input().split())
    team_1[a - 1] += 1
    team_2[b - 1] += 1

for i in range(M):
    print(team_2[i] - team_1[i])


