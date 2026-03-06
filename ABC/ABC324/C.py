"""
そのまま、一個挿入、一個削除、一個取り替えのどれか
要するにT'に対して上記の操作でできる文字列ならOK
長さの合計が5*10^5なのでO(N),O(NlogN)でやりたい
元の配列と比べたら一個以下しか違わない
双方向から走査していって一致している長さを記録(A,B)
これで判定できる、O(N)
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC324/input.txt')

N, T = input().split()
N = int(N)

ans = []

for i in range(N):
    S = input()
    A = 0
    B = 0
    for j in range(min(len(S), len(T))):
        if T[j] == S[j]:
            A += 1
        else:
            break
    for j in range(min(len(S), len(T))):
        if T[len(T) - j - 1] == S[len(S) - j - 1]:
            B += 1
        else:
            break
    #完全一致
    if A == B == len(T) == len(S):
        ans.append(i + 1)
    #一個削除
    elif A + B >= len(S) - 1 == len(T):
        ans.append(i + 1)
    #一個入れ替え
    elif A + B == len(T) - 1 == len(S) - 1:
        ans.append(i + 1)
    #一個挿入
    elif A + B >= len(S) == len(T) - 1:
        ans.append(i + 1)

    
print(len(ans))
print(*ans)
    
    

