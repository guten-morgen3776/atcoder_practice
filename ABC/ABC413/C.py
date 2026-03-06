"""
複数要素の追加と削除を高速でやりたい
基本的に一っこずつしかできないからデータの保持の仕方を工夫したい
追加の時は[数字、数]の形で追加できそう,O(1)
でも取り出す時にどうするか、結局何回もpopleft()する必要があるかも
先頭[c,x]に対してc>kの時はc-kにc<=kの時は消えなくなるまで消す
計算量はO(Q)？？
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC413/input.txt')

Q = int(input())

from collections import deque
A = deque() #[c,x] xをc個

for _ in range(Q):
    que = list(map(int , input().split()))
    ans = 0
    if que[0] == 1:
        c, x = que[1], que[2]     
        A.append([c, x])
    else:
        k = que[1]
        while A and A[0][0] <= k:
            ans += A[0][0] * A[0][1]
            k -= A[0][0]
            A.popleft()
        if A and A[0][0] > k:
            ans += k * A[0][1]
            A[0][0] -= k
        print(ans)

        


        

