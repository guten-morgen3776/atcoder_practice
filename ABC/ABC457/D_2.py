"""
解の二分探索という方法で解けるらしい
すべての要素を X 以上にするのに、必要な操作回数は K 回以下か？
"""

import sys 
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC457/input.txt')

import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

# ansをx以上にすることができるか判定する
def isok(x):
    nk = 0
    for i in range(N):
        if A[i] < x:
            # x を超えるのに最低限必要な回数
            nk += (x - A[i] + i) // (i + 1) #math.ceilを使うと浮動小数点誤差が出てしまう
            if nk > K:
                return False
    return True

# 二分探索
left = 1
right = max(A) + K + 1
while right - left > 1:
    mid = (right + left) // 2
    if isok(mid):
        left = mid
    else:
        right = mid

print(left)