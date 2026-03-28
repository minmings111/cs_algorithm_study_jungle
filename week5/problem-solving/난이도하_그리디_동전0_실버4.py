# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys

n, k = map(int, input().split())
coins = [int(sys.stdin.readline()) for i in range(n)]

seleced = 0
for i in coins[::-1]:
    temp = k//i
    if temp > 0:
        seleced += temp
        k = k%i

print(seleced)