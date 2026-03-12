# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

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