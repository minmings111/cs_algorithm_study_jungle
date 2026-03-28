# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys
strs = sys.stdin.readline().split("-")

minimum = 0
for i in range(len(strs)):
    if i == 0:
        minimum += sum(map(int,strs[i].split("+")))
    else:
        minimum -= sum(map(int,strs[i].split("+")))

print(minimum)