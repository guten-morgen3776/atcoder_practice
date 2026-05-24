"""
並び替えることで全ての隣り合う文字が異なるようにしたい　
それが可能かどうか判断する　可能かどうかの判断は個数の最大が(len(S)+1)//2 以下ならいける　これはO(L)なのでいける

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC459/input.txt')

from collections import Counter 

T = int(input())
for _ in range(T):
    S = list(input())
    c = Counter(S)
    cnt = c.most_common() #(文字, 個数) のリストで頻度順
    max_cnt = cnt[0][1]  

    if max_cnt <= (len(S)+1) // 2:
        print('Yes')
        # ここから並び替え
        #多いやつほど隣り合う危険性が高いからそいつらから並べたほうがいい
        #多いやつを先に並べてその隙間に次に多いやつを入れるというのを繰り返す
        #同じ文字を同じ隙間に入れない　個数的に必ず違うところに入れられるはず
        #多い順に偶数index埋める→奇数インデックス埋めるをやればいい
        res = [''] * len(S)
        indexs = list(range(0, len(S), 2)) + list(range(1, len(S), 2))
        pos = 0
        for char, count in cnt:
            for _ in range(count):
                res[indexs[pos]] = char
                pos += 1
        print("".join(map(str, res)))
    else:
        print('No')


