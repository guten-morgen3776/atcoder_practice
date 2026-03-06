"""
kが書かれたボールがkこ並ぶと消える
ぷよぷよ問題だからスタックに入れて消す
個数を[値、個数]としてスタックに記録しておく
すでに値が直前にあったらその個数を+1,ないなら[値, 1]としてappend
個数がkになったら[]を消す
消す回数を記録して全体から消す
"""
import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC240/input.txt')
N = int(input())
A = list(map(int, input().split()))
stack = []
idx = 0
stack.append([A[idx], 1])
cnt = 0
idx += 1
print(1)
while idx < N:
    #スタックに追加する
    if stack and stack[-1][0] == A[idx]:
        stack[-1][1] += 1
    else:
        stack.append([A[idx], 1])

    #k個揃ったら消す
    if stack[-1][0] == stack[-1][1]:
        cnt += stack[-1][0]
        stack.pop()
    print(idx - cnt + 1)
    idx += 1


    
    
    

