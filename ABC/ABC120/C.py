"""
できるだけたくさんとっていきたい、取り出せる回数って順番関係あるの？なくね？
新しいものを消すからスタック？
前から見てって隣り合ってたらそいつらを消すというのを繰り返す
"""
import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC120/input.txt')

S = list(map(int, input()))
N = len(S)
stack = []
stack.append(S[0])
cnt = 0
idx = 1
while idx < N:
    nxt = S[idx]
    if stack and stack[-1] != nxt:
        #赤と青を消す
        stack.pop()
        cnt += 2
    else:
        stack.append(nxt)
    idx += 1
print(cnt)




