"""
重心で判定すると中心付近がうまく捌き切れない
0,1について両方やればいい
中心付近の残すブロックを決められればそれより端は全部消す必要ある
消すもじ：1回、消さない文字：2回
どの文字が何連続しているかが大事だからランレングス圧縮,O(N)
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC426/input.txt')

from itertools import groupby

def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    run_S = runLengthEncode(S)
    c1 = 0
    c0 = 0
    max_1 = 0
    max_0 = 0
    for r in run_S:
        if r[0] == '1':
            c1 += r[1]
            max_1 = max(max_1, r[1])
        else:
            c0 += r[1]
            max_0 = max(max_0, r[1])
    ans = min(2 * (c0 - max_0) + c1, 2 * (c1 - max_1) + c0)
    print(ans)

        
    
    



