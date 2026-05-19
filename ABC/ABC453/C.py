"""
できるだけ0を通りたいから現在地が正なら左、負なら右方向に行けばいい
現状の座標を保持していればいいだけでは？
よく考えたら貪欲が成立しない場合もあるのでビット前探索
"""

import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC453/input.txt')

N = int(input())
L = list(map(int, input().split()))

ans = 0

for bit in range(1 << N):  
    pos = 0.5
    cnt = 0
    for i in range(N):
        pre = pos
        if (bit >> i) & 1:
            pos -= L[i]
        else:
            pos += L[i]
        if pos * pre < 0:
            cnt += 1
    ans = max(ans , cnt)
print(ans)

            