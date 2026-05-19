"""

"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC452/input.txt')

H, W = map(int, input().split())
edge = '#' * W
print(edge)
for _ in range(H - 2):
    row = '#'+ '.' * (W - 2) + '#'
    print(row)
print(edge)   