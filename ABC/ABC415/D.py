"""
シールを最大化したい,つまりできるだけ交換回数を増やしたい
一回の交換でシールは１枚、コーラの総数は+(Bi-Ai)
飲む回数はどうでもいいのでびんの総数さえ数えればいい
現在持っている瓶の数がkだとしたらk>Aiの中でBi-Aiが最大のものを選び続ける
これを毎回愚直にやるとTLE
基本的にkは単調減少→それ以上の[A,B]は削除する、O(M)でいける
あらかじめBi-Aiについての配列を優先度付きキュートして持っておけばそこから最大の要素を取り出す、O(MlogN)でいける
でも消したかどうかを連動させる必要があるから[[B-A,A],...[]]みたいな配列で持っておいて
Aについてソートすれば端から消していけばいいだけ
最大値だからB-Aは負で持っておく必要がある、つまりA-B
ソートしちゃったら優先度付きキューの内部構造が崩れるからAのリストと,A-Bのheapで分けて保持するべき
k>=Aiのやつはheapに入れる、k<AiのやつはABから消す、heapから最小のA-Bを見る（取り出さない）
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC415/input.txt')

N, M = map(int, input().split())
from collections import deque
import heapq
heap = []
AB = []

for i in range(M):
    a, b = map(int, input().split())
    AB.append([a, b])

AB.sort(key=lambda x: x[0])

AB = deque(AB)
k = N #現在のコーラの瓶の数
ans = 0

while True:
    #k>=Aならheapに入れる
    while AB and AB[0][0] <= k:
        a, b = AB.popleft()
        heapq.heappush(heap, [a - b, a])
    #heapの先頭がk<aなら捨てる
    while heap and k < heap[0][1]:
        heapq.heappop(heap)
    #heapがからならもう無理
    if not heap:
        break
    #heapから最小のA-Bをみる（取り出さない）
    diff, a = heap[0] #diffは正
    #何回交換できるか計算する k>=aであるかぎるは同じペアで交換し続ける
    cnt = (k - a) // diff + 1
    k -= diff * cnt
    ans += cnt
    #k<aになったので捨てる
    heapq.heappop(heap)

print(ans)
