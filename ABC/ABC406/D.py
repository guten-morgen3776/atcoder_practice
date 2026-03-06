"""
それぞれの行と列について落ちているゴミの数を高速で把握したい
毎回数え上げるのは無理
それぞれの列について何個あるかを保持しておくだけだとそれを捨てた時に他の部分がそれだけ減るかを管理できない
ある行を捨てるってなったらその行の合計を０にする&その行についてどの列にゴミがあったかを参照してそれぞれの列から一個ひく
これをやるのにO(H)かかるからぜんたいでO(QH)でTLE
でも結局ゴミの数の分だけ処理するだけだからO(N + Q)でいける
行->列の変換がO(1)でできればいい
一度処理した行列については確定で０だし他の部分の処理も不要、というか負になるから処理しちゃダメ
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC406/input.txt')

H, W, N = map(int, input().split())

#必要なデータ保持(1index)
row_gomi = [[] for i in range(H + 1)] #それぞれの行にあるゴミの列番号
col_gomi = [[] for i in range(W + 1)] #それぞれの列にあるゴミの行番号
row_cnt = [0] * (H + 1)
col_cnt = [0] * (W + 1)

for _ in range(N):
    x, y = map(int, input().split())
    row_gomi[x].append(y)
    col_gomi[y].append(x)
    row_cnt[x] += 1
    col_cnt[y] += 1
Q = int(input())
for _ in range(Q):
    que = list(map(int, input().split()))
    ans = 0
    if que[0] == 1:
        x = que[1]
        ans = row_cnt[x]
        if ans > 0:
            #まずその行のゴミの数を0に
            row_cnt[x] = 0
            #そのゴミの列番号についてそれぞれ個数を-1
            for i in row_gomi[x]:
                if col_cnt[i] > 0:
                    col_cnt[i] -= 1
    else:
        y = que[1]
        ans = col_cnt[y]
        if ans > 0:
            #まずその列のゴミの数を0に
            col_cnt[y] = 0
            #そのゴミの行番号についてそれぞれ個数を-1
            for i in col_gomi[y]:
                if row_cnt[i] > 0:
                    row_cnt[i] -= 1
    print(ans)
    



