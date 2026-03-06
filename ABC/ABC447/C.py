"""
Aを消すかAを好きな位置に挿入できる
つまりA以外の文字の配置が同じなら可能,O(N)でいける
最小回数はAの位置の差を考える
Aの位置を記録しておいて数の差&いちが違う個数の合計
でも挿入したら他のAの位置も変わるよね
B,Cをしきりと考えてそれぞれの間に何個入っているかを比較する
"""
import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC447/input.txt')

S = list(input())
T = list(input())

max_len = max(len(S), len(T))

S_A = [0] * max_len
T_A = [0] * max_len

# 一旦正誤判定
S_ = []
for s in S:
    if s != 'A':
        S_.append(s)
        
T_ = []
for t in T:
    if t != 'A':
        T_.append(t)
ans = 0
if S_ == T_:
    S_A = [0] * (len(S_) + 1)
    T_A = [0] * (len(T_) + 1)
    idx = 0
    for s in S:
        if s == 'A':
            S_A[idx] += 1
        else:
            idx += 1
    idx = 0
    for t in T:
        if t == 'A':
            T_A[idx] += 1
        else:
            idx += 1
    for i in range(len(S_A)):
        ans += abs(S_A[i] - T_A[i])
    print(ans)
else:
    print(-1)