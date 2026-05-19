"""
候補の文字列数はM 背骨の文字数はN
先に背骨を決めちゃう？だって長さがNじゃないといけないから絞れる

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC452/input.txt')

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

M = int(input())
str_info = set()
S = []
for _ in range(M):
    s = input()
    S.append(s)
    length = len(s)
    for i in range(length):
        str_info.add((length, i + 1, s[i]))

ans = []
for s in S:
    if len(s) != N:
        ans.append('No')
        continue
    flag = True
    for i in range(N):
        if (A[i], B[i], s[i]) not in str_info:
            flag = False
            break
    if flag:
        ans.append('Yes')
    else:
        ans.append('No')

for i in range(M):
    print(ans[i])