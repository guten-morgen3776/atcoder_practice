"""
連続部分列での各インデックスと要素の積の和の最大値
連続部分列で単調制があるから尺取りでいけるね
O(N)でいけるはず
Bの左端をスライドするときに全部のインデックスが変わるから端だけの値じゃ差分を更新できない
それぞれのインデックスが１小さくなるから区間内の和を引けばいい、つまり区間内のわも保持して進む必要がある
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC267/input.txt')

N, M = map(int, input().split())
A = list(map(int, input().split()))

from collections import deque   
"""
A: 対象の配列
K: 条件の基準となる値（例：区間の和がK以下）
"""
q = deque()
state = 0  # 区間の状態を管理する変数（和、積、要素のカウントなど）
ans = -float('inf')    # 求める答え（最大長、組み合わせ数など）
sum_ = 0

for x in A:
    # ① 右端をキューに追加し、状態を更新する
    q.append(x)
      # 例: 和を更新
    state += len(q) * x 
    sum_ += x

    # ② 条件を満たさなくなったら、満たすようになるまで左端を取り除く
    # （※キューが空でないことも必ず条件に入れる）
    while q and len(q) > M: # is_validは条件判定
        rm = q.popleft()
        state -= sum_ # 状態から左端の要素分を引く
        sum_ -= rm
        
            
    # ③ 条件を満たしている状態での処理を行う
    if len(q) == M:
        ans = max(ans, state) # 例: 条件を満たす最大長を求める
    # ans += len(q)        # 例: 条件を満たす部分列の数を数え上げる
print(ans)