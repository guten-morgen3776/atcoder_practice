"""
２進法が関係してる？
1~全部調べるのは無理

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC451/input.txt')

N = int(input())
component = []
for i in range(100):
    if 2 ** i < 10 ** 9:
        component.append(str(2 ** i))
    else:
        break

#繋げる要素数は何でもいい、長さが9以下なら何でもいい
#条件を満たす間は繋げ続ける

nums = set()
comp = component.copy()

while comp:
    s = comp.pop()
    num = int(s)
    if num > 10 ** 9:
        continue
    nums.add(num)
    for c in component:
        n_num = s + c
        if len(n_num) <= 9:
            comp.append(n_num)
ans = sorted(list(nums))
print(ans[N - 1])


