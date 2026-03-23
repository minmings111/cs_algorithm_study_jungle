# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

import sys
input = sys.stdin.readline

nn = int(input())

for i in range(nn):
    n, m = map(int, input().split())

    for j in range(m):
        a, b = map(int, input().split())

    # "모든 정점 N개"을 연결하는 최소 간선의 수는 (N - 1) => 공식!
    print(n - 1)
        
    


