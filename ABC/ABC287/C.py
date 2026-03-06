"""
パスグラフかいなか→１本だけ
枝分かれがない
M = N - 1,各頂点のつながる先が２以下、グラフが連結
３つの条件を満たせばいい
"""
import sys
sys.setrecursionlimit(10 ** 8)

#import sys 
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC287/input.txt')

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1) 

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

dfs(1, G, visited)

answer = True
for i in range(1, N + 1):
    if visited[i] == False:
        answer = False

flag = True
if M == N - 1:
    if answer:
        for i in range(N):
            if len(G[i]) > 2:
                flag = False
    else:
        flag = False
else:
    flag = False

if flag:
    print('Yes')
else:
    print('No')