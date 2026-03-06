"""
すでに連続している文字の間の同じ文字を挿入
どの文字がなんか連続しているかだけが重要
らんレングス圧縮すればいい
個数が2以上ならそれを一回の操作で増やせる
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC259/input.txt')

S = input()
T = input()

from itertools import groupby

def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

run_s = runLengthEncode(S)
run_t = runLengthEncode(T)

if len(run_s) == len(run_t):
    flag = True
    for i in range(len(run_s)):
        #そもそも文字が違う
        if run_s[i][0]  != run_t[i][0]:
            flag = False
        #文字が同じだけど個数の大小関係がおかしい
        elif run_s[i][0] == run_t[i][0] and run_s[i][1] > run_t[i][1]:
            flag = False
        #文字も大小関係もOKだが元の個数が１かつ個数が違う
        elif run_s[i][0] == run_t[i][0] and run_s[i][1] < run_t[i][1] and run_s[i][1] == 1:
            flag = False
    if flag:
        print('Yes')
    else:
        print('No')
else:
    print('No')



