"""
中央値を高速で求める
A,Bと前の中央値から次の中央値の遷移を考える
個数は常に奇数だから中央値は一つ
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC458/input.txt')

X = int(input())
Q = int(input())

mid = X
left = []
right = []

import heapq

for _ in range(Q):
    a, b = map(int, input().split())
    #両方とも中央値より大きいなら中央値は右に移行、小さいなら左に移行
    #挟んでたら不変
    #中央値、左の集合、右の集合として管理してheapqで最大最小をO(1)で取り出す
    if a >= mid and b >= mid:
        heapq.heappush(right, a)
        heapq.heappush(right, b)
        # 右の最小
        right_min = heapq.heappop(right)
        #元midをleftへ
        heapq.heappush(left, -mid)
        mid = right_min
    elif a <= mid and b <= mid:
        heapq.heappush(left, -a)
        heapq.heappush(left, -b)
        #左の最大
        left_max = -heapq.heappop(left)
        # 元midをrightへ
        heapq.heappush(right, mid)
        mid = left_max
    elif a <= mid <= b:
        heapq.heappush(left, -a)
        heapq.heappush(right, b)
    elif b <= mid <= a:
        heapq.heappush(left, -b)
        heapq.heappush(right, a)
    print(mid)

