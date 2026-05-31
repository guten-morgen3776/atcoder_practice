"""
Sj右Si左　両端同じ　長さの範囲が決まっている
その長さの区間内で同じ文字のペアがいくつあるかを事前に計算しておく
具体的には、その位置にある文字がそれ以前の文字と作るペアの個数かな？
"""
import sys
sys.stdin = open('/Users/aokitenju/Downloads/競プロ/ABC/ABC449/input.txt')

N, L, R = map(int, input().split())
S = list(input())

char_cnt = [0] * (N + 1)
already = set()














