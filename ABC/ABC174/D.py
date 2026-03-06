"""
赤い石の左隣に白い石がない状況にしたい
入れ替えるか色を返すかのどっちかを選ぶ、入れ変えるのは隣り合ってなくても良い
最終的にrrrr..rwww...wとなっていればいい
優先順位としては入れ替える>塗り替えるのはず
よくよく考えたら塗り替えるって使わなくね、入れ替えるだけで完結するよね
右から見ていってRがあれば一番左にあるWを入れ替える操作を繰り返す
そうじゃなくてR,Wの個数を数えて最終的な形との差分を考えるだけでいい？
境界線を作ってそこより右にあるRの個数が入れ返す必要がある回数
"""
import sys 
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC174/input.txt')

N = int(input())
C = list(input())
cnt_r = 0
cnt_w = 0
for c in C:
    if c == 'R':
        cnt_r += 1
    else:
        cnt_w += 1
ans = 0
for i in range(N - 1, N - cnt_w - 1, -1):
    if C[i] == 'R':
        ans += 1
print(ans)

