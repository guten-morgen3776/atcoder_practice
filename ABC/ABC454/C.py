"""
AiがあればBiが手に入る　保持できるアイテムは一個だけ
伝播していくからグラフとしてみる　一方向だから有向グラフ
その有向グラフ内で1から辿り着けるものの種類を求めればいい
bfsかな？ O(N)
"""

import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC454/input.txt')

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N + 1)]
for a, b in edges:
    G[a].append(b)

# 1から辿り着けるものの種類を求める　
start = 1

from collections import deque
d = deque()
d.append(start)

visited = set()
visited.add(start)

# bfs
while d:
    pos = d.popleft()
    for next in G[pos]:
        if next not in visited:
            visited.add(next)
            d.append(next)

ans = len(visited)

print(ans)

        
            



        
    





