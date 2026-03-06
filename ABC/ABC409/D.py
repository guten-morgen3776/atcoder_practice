"""
辞書順で最小のものさえわかればいい
操作する場所は好きに選べる
辞書順で一番後ろの文字を一番後ろに持っていけばいい
最大のものが高速で取り出せたらいい、優先度付きキューを使えばいいのかな？
O(QlogN)でいけるはず
でも反転にO(N)かかるから無理だ
そもそも最後尾に持っていくのが最適かはわからない、それの辞書順で最後のやつを動かせばいいとは限らない
どの文字をとってそれをどこに持っていくか決める
前から見ていって単調増加が途切れるタイミングの文字を動かす
その文字をどこまで持っていったらいい？？
その文字より辞書順で大きい文字が出てくるまで後ろに持っていく、あるならその文字の一個前、ないなら最後尾に持っていく
r決定にO(N),l決定にO(N),挿入O(N)それぞれ独立だからO(N)
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC409/input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    r = 0
    l = float('inf')
    for i in range(1, N):
        if S[i - 1] > S[i]:
            r = i - 1
            break
    for i in range(N):
        if S[r] < S[i]:
            l = i
            break
    #最後まで見つからなかったから最後尾に持っていく
    if l == float('inf'):
        S.append(S[r])
        S.pop(r)
    #見つかった場合はlの前に持っていく
    else:
        S.insert(l, S[r])
        S.pop(r)
    print("".join(map(str, S)))

       
            
            

        
        
    
    


        