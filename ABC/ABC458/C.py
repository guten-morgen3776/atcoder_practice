"""
条件を満たす部分文字列の数を求める
中央がCだけだからそこから広げいく感じ
Cの位置からみて左右のうち短い方+1がそのC中心の文字列の個数
これを全てのCについてやればOK
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC458/input.txt')



S = list(input())
ans = 0
for i in range(len(S)):
    s = S[i]
    #左側と右側の個数
    left = i
    right = len(S) - i - 1
    if s == 'C':
        ans += min(left, right) + 1
print(ans)

