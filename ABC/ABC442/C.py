"""
A + C + 何かでコンテストを開ける
できるだけたくさん開催したい
T回やらないといけないから一回の判別は高速じゃないとけないね
n回開催するとしたらA,Cがnこあってかつそれ以外にnこ文字を持つことが必要
最高でもmin(na, nc)
nを一減らすとそれ以外の文字数が2増える
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC442/input.txt')

T = int(input())
for _ in range(T):
    na, nb, nc = map(int, input().split())
    ans = 0
    sum_ = na + nb + nc
    n = min(na, nc)
    rem = sum_ - n * 2
    if rem >= n:
        ans = n
    else:
        if (n - rem) % 3 != 0:
            x = (n - rem) // 3 + 1
            ans = n - x
        else:
            x = (n - rem) // 3
            ans = n - x
    print(ans)


