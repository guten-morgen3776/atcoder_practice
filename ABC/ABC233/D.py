"""
条件を満たす連続部分列の数→尺取り
区間長はなんでもいい、和がKになっているペアを数える
O(N)でいける
Aって負もあるから単調性なくね？尺取りでできなくね？
和がピッタリKだから累積和とってそれについて分布を連想配列で保持しておく
Sr = Sl + Kとなる要素が何個存在するかを数える
O(N)でいけるはず
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC233/input.txt')

N, K = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)
d[0] += 1
ans = 0
cur_sum = 0
for i in range(N):
    cur_sum += A[i]
    ans += d[cur_sum - K]
    d[cur_sum] += 1
print(ans)


