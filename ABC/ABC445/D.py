"""
逆に辿っていけばいいはず
現在の縦横の長さとピースの縦横を保持しておいて辺の長さが一致するピースを見つけていけばいい
置き方はなんでもいいからとりあえず現在のミニ長方形でみて左上に配置するようにする
少なくともNかいやる必要があるから一回の検索をO(1),O(logN)でやらないとTLE
長さをkeyとして保持しておけばO(1)で検索できる
まずピースの縦横をリストで管理し
具体的には辺の長さをkey,そのピースのリストでのインデックスを要素とする辞書を縦横で二つ作る
"""
#import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC445/input.txt')

H, W, N = map(int, input().split())
pieces = []
for _ in range(N):
    h, w = map(int, input().split())
    pieces.append([h, w])

from collections import defaultdict, deque
height = defaultdict(deque)
width = defaultdict(deque)
for i in range(N):
    h, w = pieces[i][0], pieces[i][1]
    height[h].append(i)
    width[w].append(i)

ans = [[0, 0] for _ in range(N)]
cur_h = H
cur_w = W

#辺の長さが一致するものを検索
#見つかったらその分をcur_から引いてansに登録
#その要素は消す
#複数辞書から対応を持ったペアで削除するのでフラグで管理

used = [False] * N

for i in range(N):
    #最初にフラグで削除
    while len(height[cur_h]) > 0 and used[height[cur_h][0]]:
        height[cur_h].popleft()
    while len(width[cur_w]) > 0 and used[width[cur_w][0]]:
        width[cur_w].popleft()

    if len(height[cur_h]) > 0:
        piece = pieces[height[cur_h][0]]
        h = piece[0]
        w = piece[1]
        #置く場所
        h_ = H - cur_h + 1
        w_ = W - cur_w + 1
        #答え
        idx = height[cur_h][0]
        ans[idx][0], ans[idx][1] = h_, w_
        #更新
        cur_h = cur_h
        cur_w -= w
        #消す
        used[idx] = True
    else:
        piece = pieces[width[cur_w][0]]
        h = piece[0]
        w = piece[1]
        #置く場所
        h_ = H - cur_h + 1
        w_ = W - cur_w + 1
        #答え
        idx = width[cur_w][0]
        ans[idx][0], ans[idx][1] = h_, w_
        #更新
        cur_w = cur_w
        cur_h -= h
        #消す
        used[idx] = True
        
for i in range(N):
    print(*ans[i])
