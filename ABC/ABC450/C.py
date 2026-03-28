"""
連結であるか否かはdfsで判断？
それの経路を保持しておいてその経路に箸が含まれるかを判定する
これ愚直にやってもTELしなくね
白かつ訪問なしなら探索開始、dfs bfsで見ていって端が一回も検出されなければans+=1
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC450/input.txt')

H,W = map(int, input().split())
S = [] #０index
for _ in range(H):
    row = list(input())
    S.append(row)

ans = 0

visited = []
for _ in range(H):
    row = [False] * W
    visited.append(row)

from collections import deque
q = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == '.' and visited[i][j] == False:
            #ここで一つの連結全体に対して検出
            #連結全体を見て逐一そこが端かいなかをチェックする
            flag = True
            q.append([i, j])
            visited[i][j] = True
            while q:
                r, c = q.popleft()
                if r == 0 or r == H - 1 or c == 0 or c == W - 1:
                    flag = False
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W:
                        # 白マスかつ未訪問なら探索候補に追加
                        if S[nr][nc] == '.' and visited[nr][nc] == False:
                            visited[nr][nc] = True
                            q.append([nr, nc])
            if flag:
                ans += 1

print(ans)

                    





