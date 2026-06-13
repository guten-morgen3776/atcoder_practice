"""
領域内の１の和がKになる領域の数が知りたい
まず片方の辺に対して和がK以上になる区間を尺取りで探す
その上でその区間を固定して、もう一方の辺を和がKになるように狭めていく
１次元に落とし込めれば尺取りでO(N)なはず
"""

import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC461/input.txt')

H, W, K = map(int, input().split())
grid = []
for _ in range(H):
    row = list(map(int, input()))
    grid.append(row)




    
        


