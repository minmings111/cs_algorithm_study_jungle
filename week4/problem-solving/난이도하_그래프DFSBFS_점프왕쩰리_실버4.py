# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

from collections import deque

n = int(input())
game_setting = [list(map(int, input().split())) for i in range(n)]

visited = [[0]*n for i in range(n)] # 초기화
visited[0][0] = 1 # 이미 간 곳 마킹
que = deque([(0,0)])

# while-else문 활용!
# 조건 내에서 break로 탈출하면 else 실행x
while que:
    r, c = que.popleft()

    if (r, c) == (n-1, n-1): # 성공 케이스
        print("HaruHaru")
        break

    jump = game_setting[r][c] # 현재 위치의 vlaue 꺼내기

    # 다음 이동칸 계산하기
    nr1, nc1 = r + jump, c # 좌로 점프
    nr2, nc2 = r, c + jump # 우로 점프

    # 이동하기 전에 체크
    # 점프할 위치가 배열 내에 위치하는가?       / 탐색 여부 체크
    if 0 <= nr1 < n and 0 <= nc1 < n and visited[nr1][nc1] == 0:
            visited[nr1][nc1] = 1 # 마킹!
            que.append((nr1, nc1))

    if 0 <= nr2 < n and 0 <= nc2 < n and visited[nr2][nc2] == 0:
            visited[nr2][nc2] = 1
            que.append((nr2, nc2))

else:
    print("Hing")





