"""
M種類以上の宝石を選ぶという条件下で価値の和を最大化する
とりあえずそれぞれの種類ごとに分けた上で最大価値でソートして上からM個を取って
それ以降はなんでもいいので上から取っていけばいいはず
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC461/input.txt')

N, K, M = map(int, input().split())
c_v = []
for _ in range(N):
    c, v = map(int, input().split())
    c_v.append([c, v])

# 色ごとにサブグループに分ける
already_c = set()
sub_grs = [] # [[c, [価値の配列]], []]
c_v.sort(key=lambda x: x[0])
for i in range(N):
    c, v = c_v[i]
    if c in already_c:
        sub_grs[-1][1].append(v)
    else:
        sub_grs.append([c, [v]])
        already_c.add(c)

ans = 0
max_cv = []
# それぞれの色の価値配列をソートする
for i in range(len(sub_grs)):
    sub_grs[i][1].sort()
    # 最大のvを上位M色で取り出す
    max_v = sub_grs[i][1].pop()
    max_cv.append([sub_grs[i][0], max_v])

#  最大のvを上位M色で取り出す
max_cv.sort(key=lambda x: x[1])
for i in range(M):
    ans += max_cv.pop()[1]

# 残りのK - M個は残りのvから上から順に選ぶ
rem_vs = []
for i in range(len(max_cv)):
    rem_vs.append(max_cv[i][1])
for i in range(len(sub_grs)):
    rem_vs += sub_grs[i][1]

rem_vs.sort(reverse=True)
for i in range(K - M):
    ans += rem_vs[i]

print(ans)


    






