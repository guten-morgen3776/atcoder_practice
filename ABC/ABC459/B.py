"""

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC459/input.txt')

N = int(input())
S = list(map(str, input().split()))
C = []

for i in range(N):
    s = S[i]
    if s[0] in 'abc':
        c = 2
    elif s[0] in 'def':
        c = 3
    elif s[0] in 'ghi':
        c = 4
    elif s[0] in 'jkl':
        c = 5
    elif s[0] in 'mno':
        c = 6
    elif s[0] in 'pqrs':
        c = 7
    elif s[0] in 'tuv':
        c = 8
    elif s[0] in 'wxyz':
        c = 9
    C.append(c)
print(''.join(map(str, C)))