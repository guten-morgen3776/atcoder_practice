"""
先頭or末尾から削除したいからdeque
最終的に同じ文字にしたい、できるだけ少ない操作で
0,1どっちの方が中心よりか調べる、両端から調べていけばいい
いくつかは2回変換して元に戻す必要がある、その場合は外側に挿入すれば一回操作を増やすだけ
どっちの方が端か定量化する必要がある、これはO(N)

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC426/input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())

    #０、１どっちが端か算出
    edge_score_0 = 0
    edge_score_1 = 0
    if N % 2 == 0:
        for i in range(N // 2):
            if S[i] == '1':
                edge_score_1 += i + 1
            else:
                edge_score_0 += i + 1

            if S[N - i - 1] == '1':
                edge_score_1 += i + 1
            else:
                edge_score_0 += i + 1
    else:
        for i in range(N // 2): #中心を含めない、後で計算
            if S[i] == '1':
                edge_score_1 += i + 1
            else:
                edge_score_0 += i + 1

            if S[N - i - 1] == '1':
                edge_score_1 += i + 1
            else:
                edge_score_0 += i + 1
        if S[(N + 1) // 2] == '1':
            edge_score_1 += (N + 1) // 2
        else:
            edge_score_0 += (N + 1) // 2

    #スコアからどっちを消すか決める
    #実際に削除したり挿入する必要はなくて、消す数字なら真ん中に挿入(もう操作しない)
    #消さない数字なら端に挿入して、もう一回操作
    #これを中心まで繰り返す、O(N)
    delete_num = float('inf')
    if edge_score_0 <= edge_score_1:
        delete_num = '0'
    else:
        delete_num = '1'
    
    ans = 0
    #必要なくなったら止める処理が必要だからどこまでやるか事前に調べる必要ある
    #左右別々でやる必要あり
    if edge_score_0 > 0 and edge_score_1 > 0:
        right_range = 0
        left_range = 0
        for i in range(N // 2):
            if S[i] == delete_num:
                left_range = max(left_range, i)
            if S[N - i - 1] == delete_num:
                right_range = max(right_range, i)

        for i in range(left_range + 1):
            if S[i] == delete_num:
                ans += 1
            else:
                ans += 2
        for i in range(right_range + 1):
            if S[N - i - 1] == delete_num:
                ans += 1
            else:
                ans += 2
        
    print(ans)
    



