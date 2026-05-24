"""
Kがどの文字列グループかと繰り返しのどの部分に当たるかが知りたい
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC457/input.txt')

N, K = map(int, input().split())

L = []
A = []
ans = 0

for i in range(N):
    row = list(map(int, input().split()))
    L.append(row[0])
    A.append(row[1:])

C = list(map(int, input().split()))

# どの文字列グループか調べる
cur_gro = 0
while K > 0:
    K -= L[cur_gro] * C[cur_gro]
    cur_gro += 1

# -Kがとりすぎたたぶん
if K == 0:
    ans = A[cur_gro-1][-1] #前のグルの最後尾
else:
    # 繰り返しのどの位置か調べる あまりを調べる
    l = L[cur_gro-1]
    rem = (-K) % l
    ans = A[cur_gro-1][l-rem-1]

print(ans)





