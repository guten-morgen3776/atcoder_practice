"""
条件を満たす部分列の個数→尺取りっぽい？
でも隣と比べて増加してるか減少してるかだけがわかればいい
+ -> -,- -> + の時に極地
区間内に極地が二つ存在すればいい
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC406/input.txt')

from itertools import groupby

def runLengthEncode(S: list):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

N = int(input())
P = list(map(int, input().split()))

diff = []
for i in range(1, N):
    if P[i - 1] < P[i]:
        diff.append('+')
    else:
        diff.append('-')

run_diff = runLengthEncode(diff)

from collections import deque
q = deque()

ans = 0

for r in run_diff:
    q.append(r)
    while (q and q[0][0] == '-') or (q and len(q) > 3):
        q.popleft()
    if len(q) == 3 and q[0][0] == '+' and q[1][0] == '-' and q[2][0] == '+':
        ans += q[0][1] * q[2][1]
    
print(ans)
