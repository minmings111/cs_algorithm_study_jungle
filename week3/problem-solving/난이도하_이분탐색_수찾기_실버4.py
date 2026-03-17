# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920


n = int(input())
num_list = list(map(int, input().split()))

t_n = int(input())
t_list = list(map(int, input().split()))

num_list.sort()


def find_target(i, num_list):
    right = len(num_list)-1
    left = 0

    while left <= right:
        mid = (left + right) // 2

        if i == num_list[mid]:
            return 1
        elif i < num_list[mid]:
            right = mid - 1
        elif i > num_list[mid]:
            left = mid+1

    return 0

for j in t_list:
    print(find_target(j, num_list))
