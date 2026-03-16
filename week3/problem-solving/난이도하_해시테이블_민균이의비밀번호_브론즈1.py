# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

input_len = int(input())
input_val = [input() for i in range(input_len)]

def find_mid_str(input_str):
    for i in input_str:
        if i[::-1] in input_str:
            pw = i
            mid = len(pw)//2
            print(len(pw), pw[mid])
            return

find_mid_str(input_val)