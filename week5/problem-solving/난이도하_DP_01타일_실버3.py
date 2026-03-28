# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

import sys
n = int(sys.stdin.readline())

bineary = [0,1,2]

for i in range(3, n+1):
    bineary[i%3] = (bineary[(i-1)%3] + bineary[(i-2)%3]) % 15746
print(bineary[n%3])