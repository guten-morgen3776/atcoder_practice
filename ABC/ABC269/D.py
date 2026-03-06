"""
幾つの連結成分を持つか求める
連結かどうかだからDFSかUFかな？
繋がっているってことは6方向のどこかが連続しているってことだよね
グループの数だからUFで行けるならそっちがいい
N < 1000だから制約が緩い、全ペアについてつなげてもO(N^2)だからいける
UFの方もO(logN)だから余裕
"""
import sys
#sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC269/input.txt')

#UFのクラス
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
    
    def group_count(self): #グループの総数を返す
        return sum(x < 0 for x in self.parents)
    
    
		

N = int(input())
grid = []

for _ in range(N):
    x, y = map(int, input().split())
    grid.append([x, y])

uf = UnionFind(N)
ans = 0
if N == 1:
    ans = 1
else:
    for i in range(N - 1):
        for j in range(i + 1, N):
            #隣り合っているか判定
            xi, yi = grid[i][0], grid[i][1]
            xj, yj = grid[j][0], grid[j][1]
            if (xi == xj and abs(yi - yj) == 1) or ((yi == yj and abs(xi - xj)) == 1) or (xi - xj == 1 and yi - yj == 1) or (xi - xj == -1 and yi - yj == -1):
                uf.union(i, j)
    ans = uf.group_count()
print(ans)



            

