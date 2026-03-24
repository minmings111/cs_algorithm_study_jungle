# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
from collections import deque

n = int(input())
edge = [list(map(int, input().split())) for i in range(1, n)]

tree = {i:[] for i in range(1, n+1)}

# connect node
for u, v in edge:
    tree[u].append(v)
    tree[v].append(u)

# 노드 방문 시, 자신의 위치에 부모의 노드를 기록
visited = [0]*(n+1)
visited[1] = 1
que = deque([1])

while que:
    curr = que.popleft()
    for i in tree[curr]:
        if visited[i] == 0:
            que.append(i)
            visited[i] = curr

for i in visited[2:]:
    print(i)