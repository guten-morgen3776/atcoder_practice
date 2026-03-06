"""
10進法で回文かどうかはすぐに判定できる、回文だから桁数は奇数じゃないといけない
A進法に直せば判定はできる
でも毎回直してたら無理
というかそもそもN < 10^12だから全てのNについて探索することはできない
10進数で回文のやつだけを探索するなら10^7のはず
10進数からA進数への変換を高速で行う必要がある、変換はO(logX)でできる
10^7*log10^12でギリなんとかなるか？
回文判定の計算量はO(1)の定数倍でいけるはず
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC414/input.txt')

import numpy as np
import math

A = int(input())
N = int(input())

ans = 0

#奇数桁数では真ん中はなんでもいい
#偶数桁では真ん中まで見る
#１桁は別途実装

#どちらにしろN以下で最大の回文を見つけないといけない

max_kaibunn = 0
for i in range(N, 0, -1):
    i = str(i)
    keta = len(i)
    if keta == 1:
        max_kaibunn = i
        break
    elif keta % 2 == 0:
        flag = True
        for j in range(0, keta // 2):
            if i[j] != i[keta - j - 1]:
                flag =  False
        if flag:
            max_kaibunn = i
    else:
        flag = True
        for j in range(0, keta // 2):
            if i[j] != i[keta - j - 1]:
                flag =  False
        if flag:
            max_kaibunn = i

if len(max_kaibunn) > 1:
    max_side = max_kaibunn[:len(max_kaibunn) // 2]




for i in range(int(max_side)):
    if i == 0:
        for j in range(10):
            j_A = np.base_repr(j, base=A)
            flag = True
            for k in range(0, len(j_A) // 2):
                if j_A[k] != j_A[len(j_A) - k - 1]:
                    flag = False
            if flag:
                ans += 1

        #元の回文が奇数

        #元の回文が偶数



















    





    