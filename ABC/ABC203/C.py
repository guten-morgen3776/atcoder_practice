"""
普通に問題文の通りに推移を追うだけでは？
友人がいるならお金をもらって、一円払って次に行く
でも愚直に追っていくと余裕でTLE
友人に会えるかどうかの判断ができればいいから
次の友人までの距離と現在の所持金を比較して
辿り着けるなら(現在-距離＋もらう金)ったやって友人元へワープ
コレならO(N)でいける
まずAについてソートしないといけないね
"""
import sys 
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC203/input.txt')
N, K = map(int, input().split())
cur_money = K
cur_pos = 0
village = []
for _ in range(N):
    a_, b_ = map(int, input().split())
    village.append([a_, b_])

village.sort(key=lambda x: x[0])

for i in range(N):
    a, b = village[i][0], village[i][1]
    dist = a - cur_pos
    if dist <= cur_money:
        cur_money -= dist
        cur_money += b
        cur_pos = a
    else:
        cur_pos += cur_money
        cur_money -= dist
        break

if cur_money > 0:
    cur_pos += cur_money
print(cur_pos)

    
