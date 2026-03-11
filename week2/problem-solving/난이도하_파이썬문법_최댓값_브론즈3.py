# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

input_val = [int(input()) for i in range(9)]

def find_max(nums):
    max_val = max(nums)
    for i in range(len(nums)):
        if max_val == nums[i]:
            idx = i+1
    print(max_val)
    print(idx)

find_max(input_val)