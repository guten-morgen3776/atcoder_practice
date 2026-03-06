"""
Aの要素は自由に並び替えられる
つまり(Aj+Bi)modMが最小になるように並び替える、トレードオフが存在しないから局所的最適解を選び続ければいい
でも毎回全てのペアについて試すとTLE
O(N),O(NlogN)で処理したい
AjmodM >= M - BimodMで最小のAjを毎回見つければいい、これはソートして二分探索
O(NlogN)でできる
でも一度使ったAは使えないよね、消す必要ある？
そもそもA,BどちらもM以下だからBを逆にソートしておけばいい？
でもBに同じ数が複数ある場合は絶対被るよね
そもそも二分探索ではないのでは？
AをソートBを逆ソートしておいて両方とも一回左から舐めてA+Bが初めてMを超えたタイミングでとるというのを続ければいい
でもMを超えない場合もあるよね、その時は終着点で取ればいいか
これならO(N)でいける、でも一回の走査で終わるのか？おわらないよね、それじゃ消さないといけない問題は解決できてないじゃん

A >= M - Bを満たす中で最小のAを見つける、
条件を満たさなくなったら切り替えつ必要がある、できるだけ小さいAとマッチさせたい
どちらにしろ小さいもの同士をマッチさせたい、和がMを超えるならmodMでやった後の最小が欲しい
つまりA B両方ソートして片方をスライドさせていけばいい、片方は２つ繋げておけば余った分ともマッチできる
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC416/input.txt')

T = int(input())

from collections import deque

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #A + B >= Mを超えるペアを最大化したい
    #AをソートBを逆ソートしてdeque化
    #足してペアになるかどうか判定してならないなら片方をpopleft、なるなら両方popleft

    Ad = deque(sorted(A))
    Bd = deque(sorted(B, reverse=True))

    pairs = 0

    while Ad and Bd:
        if Ad[0] + Bd[0] >= M:
            pairs += 1
            Ad.popleft()
            Bd.popleft()
        else:
            Ad.popleft()
    
    ans = sum(A) + sum(B) - pairs * M
    print(ans)
    






    
    

    
    

    
    
    





