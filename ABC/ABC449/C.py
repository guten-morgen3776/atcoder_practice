"""
左端を固定した上で範囲内に同じ文字が何個あるかを高速で知りたい
どの文字がどの位置までに何個あるという個数リストを予め作っておけばO(1)で求められる
個数リストはO(N)で作れる
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC449/input.txt')

N, L, R = map(int, input().split())
S = list(input())

# 文字ごとの個数リストを作成
char_cnt = [[0] * 26 for _ in range(N)]

def char_to_num(c: str) -> int:
    return ord(c) - ord('a')

for i in range(N):
    s = S[i]
    num_s = char_to_num(s)
    char_cnt[i][num_s] += 1

for i in range(26):
    for j in range(1, N):
        char_cnt[j][i] += char_cnt[j-1][i] 

for _ in range(R):
    char_cnt.append(char_cnt[-1])

# サタンを固定して範囲内に同じ文字が何個あるか数える
ans = 0
for i in range(N):
    s = S[i]
    num_s = char_to_num(s)
    range_l = i + L
    range_r = i + R
    ans += char_cnt[range_r][num_s] - char_cnt[range_l - 1][num_s]

print(ans)

















