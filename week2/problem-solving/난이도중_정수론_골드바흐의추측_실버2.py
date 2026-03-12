# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

def repeat(str_list):
    n_repeat = int(str_list[0])
    temp_str = ""
    
    for i in range(len(str_list[1])):
        temp_str += ((str_list[1][i])*n_repeat)
    
    print(temp_str)


n = int(input())
for i in range(n):
    temp = list(input().split())
    repeat(temp)

