"""
分裂が起きるのは一回だけ
つまりそのままor二つ足したらL
全て分裂したパターンと一部は分裂しなかったパターンがある
一部分裂しなかったらL = max(A),①
全て分裂したならソートして最大と最小の和がL②
どっちか判別する必要があるよね
①では最大のものを取っ払って②と同じように考えればいい
そもそもLの候補はmax(A),max(A)+min(A)の二つしかない
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC444/input.txt')

N = int(input())
A = list(map(int, input().split()))

A.sort()

candidate = []
candidate.append(max(A) + min(A))
candidate.append(max(A))

ans = []

#候補が条件を満たすかチェック
#両端からとっていって和が一定ならOK
#全部分裂しているなら要素数は偶数
if len(A) % 2 == 0:
    L = A[0] + A[-1]
    flag = True
    for i in range(N // 2):
        if L != A[i] + A[N - i - 1]:
            flag = False
    if flag:
        ans.append(L)

#まず最大値を取っ払う
for i in range(N):
    if A[N - i - 1] == candidate[1]:
        A.pop()
    else:
        break

if A and len(A) % 2 == 0:
    L = A[0] + A[-1]
    if A[0] + A[-1] == candidate[1]:
        flag = True
        for i in range(len(A) // 2):
            if L != A[i] + A[len(A) - i - 1]:
                flag = False
        if flag:
            ans.append(L)
elif len(A) == 0:
    ans.append(candidate[1])

ans.sort()
print(*ans)