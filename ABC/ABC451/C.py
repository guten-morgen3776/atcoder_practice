"""
一定の長さ以下のやつを全部削除
長さについて管理しておけばいい
長さについてをkeyとしたdictを持ってそれに対して累積和
最後に一括で引いて0以上のものだけ足し合わさればいいのかな？
違う　その時点での本数を把握しておく必要があるから最後に一括計算じゃだめ

優先度付きキューを使って最小値がh以下なら除き続ける、木の本数はQだからO(QlogQ)
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC451/input.txt')

Q = int(input())

import heapq
heap = []
cnt = 0

for _ in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        heapq.heappush(heap, que[1])
        cnt += 1
    else:
        h = que[1]
        #最小値を見てそれがh以下なら取り出し続ける
        while heap and heap[0] <= h:
            heapq.heappop(heap)
            cnt -= 1
    print(cnt)
