"""
互いにその判定
愚直にやるとN*M回やる必要がある、TLE
GCDを求めるにはユーグリッド互除法でO(log(A+B)),でもこれをN*M回やるのは無
エラトステネスの篩なら範囲内の素数を一気に求められる
素数判定と互いに素を何かしらの方法で繋げたい
Aiについて素因数分解してAの素因数の集合を作る、重複はいらないからsetで管理、
要素数は最大でもmax(A)、要素はすべて素数
その集合について1~Mで要素の倍数を消していく、素因数集合と互いにそな要素だけ残る
素因数分解がO(Nsqrt(A)),エラトステネスはO(M)に近い
"""
#import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC215/input.txt')

N, M = map(int, input().split())
A = list(map(int, input().split()))

#素因数分解
def prime_factorization(n):
    factors = []
    
    # 2で割れるだけ割る（偶数処理の最適化）
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # 3以上の奇数で割っていく
    f = 3
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f
        else:
            f += 2  # 偶数はスキップ
            
    # 最後に残った数が1でなければ、それも素因数
    if n != 1:
        factors.append(n)
        
    return factors

factors = []
for i in range(N):
    result = prime_factorization(A[i])
    for j in result:
        factors.append(j)
factors = set(factors)

#篩にかける
is_coprime = [True] * (M + 1)

for p in factors:
    # range(開始, 終了, ステップ) を使うと簡単に倍数を列挙できます
    for i in range(p, M + 1, p):
        is_coprime[i] = False

ans = []
for i in range(1, M + 1):
    if is_coprime[i]:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)