"""
部分木って何？
毎回探索するのは無理だから事前に探索してどれがどれの根かという関係を記録しておく必要がある
dfsで根から進んでいって行き止まりになって戻ってくる地点がその頂点の根
根の根は根だからその関係性も示す必要がある
行き止まりになるまでに通った経路はその頂点の根の集合→それを保持して各頂点に記録すればいい
コレだと足し算する時に[枝→根]の順番になるから遅くなる、[根→枝]に変換する必要がある
でも仮に変換しても最悪O(NQ)でTLE
dfsしながら足し算する必要がある、探索中に枝に行くときは根の値を足す
"""

#import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC138/input.txt')

import sys
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(N - 1)]

G = [list() for i in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

#頂点の値記録用の配列
value = [0] * (N + 1)
for _ in range(Q):
    p, x = map(int, input().split())
    value[p] += x
    
visited = [False] * (N + 1)

from collections import defaultdict

def dfs(pos, path):
    # 【ブロック1】 終了条件・ゴール判定（Base Case）
    # if 終了条件:
    #     return
    # 【ブロック2】 次のステップへの遷移（Recursive Step）
    for nxt in G[pos]:
        if visited[nxt]:
            continue # 訪問済みならスキップ
                        
        # 状態を進める
        visited[nxt] = True
        path.append(nxt)
        value[nxt] += value[pos]
              
        # 再帰呼び出し
        dfs(nxt, path)
              
        # 状態を戻す（バックトラック）
        visited[nxt] = False
        path.pop()

# 始点の設定とDFSの開始
start_node = 1
visited[start_node] = True
dfs(start_node, [start_node])

ans = value[1:]
print(*ans)

