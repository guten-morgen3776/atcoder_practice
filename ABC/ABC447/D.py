"""
元の配列からA,B,Cを取り除く
大事なのはそれぞれが何個存在しているかと、どこに存在しているか
愚直にやるなら一番右のA、次にそれより左で一番右のB,次にCって感じで取っていく
ABCの位置インデックスをそれぞれ配列に記録しておけば二分探索でいけるのでは？
それで該当するものがなくなったらその時点で終了
O(NlogN)かな？
使ったやつを消さないといけない
whileで小さいやつ全部消すまで足止めすればいい、O(N)
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC447/input.txt')
from collections import deque

S = list(input())

#位置を配列に記録
A = deque()
B = deque()
C = deque()
for i in range(len(S)):
    if S[i] == 'A':
        A.append(i)
    elif S[i] == 'B':
        B.append(i)
    else:
        C.append(i)
#ABCはソートずみ
ans = 0

for i in range(len(A)):
    a = A[i]
    #Bの中でaより大きい最小値を探す,それより小さいものは全部消す
    while B and B[0] <= a:
        B.popleft()
    if not B:
        break
    b = B.popleft()
    while C and C[0] <= b:
        C.popleft()
    if not C:
        break
    C.popleft()
    ans += 1
print(ans)


