"""

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC447/input.txt')

from collections import Counter
S = list(input())
cnt = Counter(S)

max_cnt = 0
max_ = []
for i in S:
    if cnt[i] > max_cnt:
        max_cnt = cnt[i]
for i in S:
    if cnt[i] == max_cnt:
        max_.append(i)
        
ans = []

for i in range(len(S)):
    if S[i] not in max_:
        ans.append(S[i])
print(''.join(map(str, ans)))

