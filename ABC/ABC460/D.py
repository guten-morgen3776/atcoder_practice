"""
多分規則性を見つける問題　収束するはずだから
一度白になる&隣接に黒なし→ずっと白
黒は必ず次白になる
最後は２パターンを交互に繰り返す　それまでは拡大を続ける
白黒を繰り返すようになったらそこで決まる　その時の手数が偶数か奇数かで決まる
最初に黒の位置から黒が全範囲を網羅するまでのターン数とその時の配置が知りたい
それぞれの白から黒まで最小移動でいける回数が知りたいのでBFSかな？でも全部の白に対してやってたら間に合わないよな
→多点BFSならいける　これで最初に黒になる回数d[i][j]を求める
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC460/input.txt')

H, W = map(int, input().split())
grid = []
for _ in range(H):
    row = list(input())
    grid.append(row)

# 多点BFS
d = [['NAN'] * W for _ in range(H)]

from collections import deque 

q = deque()

# まず黒い点を全部キューに入れてd=0にする
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            d[i][j] = 0
            q.append([i, j])

# BFS本体
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and d[nx][ny] == 'NAN':
            d[nx][ny] = d[x][y] + 1
            q.append([nx, ny])


# d[i][j]の偶奇で分ける 偶数なら黒で奇数なら白
ans = []
for _ in range(H):
    row = [0] * W
    ans.append(row)

for i in range(H):
    for j in range(W):
        if d[i][j] % 2 == 0 and d[i][j] != 'NAN':
            ans[i][j] = '#'
        else:
            ans[i][j] = '.'

for i in range(H):
    row = ans[i]
    print(''.join(row))


