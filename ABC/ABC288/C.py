"""
閉路の数だけ辺を消さなサイクルはなくなる
サイクルの数を求めればいい
サイクル検出はUF

"""
#import sys 
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC288/input.txt')

class UnionFind:
    def __init__(self, n):
        #親要素のノード番号を格納　根は−１
        self.parents = [-1] * n
        
    def find(self, x): #各番号の根がどれかを探す
        if self.parents[x] < 0:
            return x
        else:
            #再起処理　親の親とたどって根を見つける
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
            
    def union(self, x, y):
        #お互いの根を呼び出す
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            #parentsの値はマイナス　絶対値が人数
            x, y = y, x
        self.parents[x] += self.parents[y]  
        self.parents[y] = x
        return True
    
    def is_same(self, x, y): #つながっているかどうかを返す
        return self.find(x) == self.find(y)
    
    def size(self, x): #グループのメンバー数を返す
        return -self.parents[self.find(x)]
	
N, M = map(int, input().split())
uf = UnionFind(N + 1)
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    if uf.is_same(a, b):
        ans += 1
    uf.union(a, b)
print(ans)
    
    


