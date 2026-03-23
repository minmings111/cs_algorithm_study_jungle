# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
from collections import deque

n = int(input())

temp = int(input())
network = [tuple(map(int, input().split())) for i in range(temp)]

graph = {i:[] for i in range(1, n+1)}

for u, v in network:
    graph[u].append(v)
    graph[v].append(u) # 양방향!

visited = []

que = deque([1])
visited.append(1)

while que:
    temp = que.pop()
    for i in graph[temp]:

        if i not in visited:
            visited.append(i)
            que.append(i)


print(len(visited)-1)

