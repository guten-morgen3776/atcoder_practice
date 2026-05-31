"""
シャリとネタを組み合わせてできるだけ多くの寿司を作りたい
ネタの重さ<=シャリの重さ*2
コレ貪欲でいける？
シャリ目線で少ない方を起点にソートして小さいものから作っていく
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC460/input.txt')


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0 
ans = 0
A.sort()
B.sort()
from collections import deque
B = deque(B)
# Bの中で2*ai以下の要素で最小のものを選び続ける
# 選ばないものは消す
while i < len(A) and B:
    #ペアがAで埋まるorBがなくなるまで続ける
    a = A[i]
    if B[0] <= 2 * a:
        i += 1
        ans += 1
        B.popleft()
    else:
        i += 1

print(ans)



        




