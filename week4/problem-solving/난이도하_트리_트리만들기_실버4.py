# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split()) # 4, 2

leaf_count = 0
last_node = 0

for i in range(1, n):

    if leaf_count < m:
        print(0, i)
        leaf_count += 1
        last_node = i
    else:
        print(last_node, i)
        last_node = i