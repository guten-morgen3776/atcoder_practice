"""
数列の中で最大のものとその次に大きいものを把握して、２番目を最大に足すをくりかえす
最大はheapqで取り出せるし２番目はそれを2回やればいけるはず
足し算した後ものの数列にpushすればOK

違うわ　最小値を最大化したいのか　それに足すのは数列の要素じゃなくてインデックス
一番小さいものにそのインデックスを足す操作を繰り返せばいい　heapqで最小値を取り出すことはできるが元インデックスを保持しておきたい
heapqの要素を[val, idx]にすればいい
毎回繰り返すとO(KlogN)になって思いっきりTLEなので最小が変わらない間のidx足し算を一括でできるようにしないといけない
つまり最小とその次の最小の差分を把握して何回足したら最小が入れ替わるか把握する必要がある

よくよく考えたらこの方法でも最悪計算量はTLEだ　他の方法が必要
"""
import sys 
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC457/input.txt')

import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))

heap = []
for i in range(N):
    heapq.heappush(heap, [A[i], i + 1]) # heapqの要素を[val, idx]にする

# 一番小さいものにそのインデックスを足す操作を繰り返す
# 最小とその次の最小の差分を把握して何回足したら最小が入れ替わるか把握する
iter = 0
while iter < K:
    fir_min = heapq.heappop(heap)
    if not heap:
        fir_min[0] += (K - iter) * fir_min[1]
        heapq.heappush(heap, fir_min)
        break
    sec_min = heapq.heappop(heap)
    diff = sec_min[0] - fir_min[0]
    change_iter = max(1, (diff + fir_min[1] - 1) // fir_min[1])
    if iter + change_iter > K:
        new_iter = K - iter
        fir_min[0] += new_iter * fir_min[1]
        heapq.heappush(heap, fir_min)
        heapq.heappush(heap, sec_min)
        iter += new_iter
    else:
        fir_min[0] += change_iter * fir_min[1]
        heapq.heappush(heap, fir_min)
        heapq.heappush(heap, sec_min)
        iter += change_iter
print(heap[0][0])









    




