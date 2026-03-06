"""
伝播の関係だからグラフで考える
繋げた時に同じグループに友達がいないようにしたい
メンバーが最大の集団をバラバラにすればいい
最大のメンバー数が答え
UFでできる？
"""
#import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC177/input.txt')

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
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.parents[self.find(x)]
	
import sys	 	
sys.setrecursionlimit(10**6)
	
N, M = map(int, input().split())
uf = UnionFind(N + 1)
for _ in range(M):
	a, b = map(int, input().split())
	uf.union(a, b)
size = []
for i in range(N):
	size.append(uf.size(i + 1))
print(max(size))

	
