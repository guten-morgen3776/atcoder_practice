"""
中にいる団体の人数がK以下、つまり入っても煽れないなら集団は入る
つまり現在入れるなら入るそうでないなら入らないのどっちかを判断できればいい
中にいる人数は常に保持する必要あり
入った時点で出る時間は確定する、
時間と出る人数を記録した連想配列を作る、これは入店した瞬間に書き込む
でもそれに加えて行列に誰がいるかとその順番を把握しておく必要ある
時系列で流れるからdeque,保持したい情報は誰か、人数
入れるならpopleft、入れないならそのまま、きた時に入れないならappend
入る時間は行列に加わった時点で確定する、それ以降は考慮する必要はない
入った時点の行列、中の人数で入る時間は求められる

そもそも行列の管理は必要ない、誰がいつ入るか、いつ出るかと言うのを順番に処理するだけ
退出時間を管理するときに最小の時間を高速で取り出したい→heapqを使う
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC423/input.txt')

import heapq
expire = [] #退出時間、人数

N, K = map(int, input().split())

t = 0
cur_num = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    t = max(t, a)
    #tで退店処理
    while expire and expire[0][0] < t:
        t_out, c_out = heapq.heappop(expire)
        cur_num -= c_out
    #まだ入れないなら次の退店時間へジャンプ
    while cur_num + c > K:
        t_out, c_out = heapq.heappop(expire)
        t = t_out
        cur_num -= c_out
    #入店
    cur_num += c
    heapq.heappush(expire, (t + b, c))
    print(t)









    

    
    

