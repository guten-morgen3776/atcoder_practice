"""
毎年石の受け渡しが行われるからしミューレーション的にとく
i年ごではそれ以外で一っこ以上持ってるやつがAiに渡す
つまりAi > 0の個数を常に保持しておく必要がある
範囲内に一括で引き算するからいもす使う、でも0かどうかも考慮しないといけないから一括はダメか
でも成人しか渡さないからそれ以前の要素しか考慮しなくていい
配列は逐次更新していかないと追えないよね
でももらうのは成人になるときの１度だけだからそのとき何個もらうのかどうかが分かればその範囲に一括足し算すればいいかわかる
何個もらうのかはその前の配列の状態を把握してないといけない
端から走査していって０になっているかを管理する配列を更新していく、もらったやつはいつゼロになるかわかるからそこに書き込む
もらう時はそれ以前で配列を見て0じゃないやつの個数ぶんをたす
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC388/input.txt')

N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

active = 0 #新成人に配れる大人の人数
expires = defaultdict(int) #配れなくなるタイミング
B = A.copy()

for i in range(N):
    #最大所持数
    active -= expires[i]
    M = A[i] + active
    #更新
    if M > 0:
        active += 1
        expires[i + M + 1] += 1

    #配列操作
    fin = min(i + M + 1, N)
    B[i] = M - (fin - i) + 1
print(*B)

    




