# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

from math import sqrt

input_count = int(input())
input_val = list(map(int, input().split()))


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for j in range(3, int(sqrt(n))+1, 2):
        if n % j == 0:
            return False
    return True

def count_prime(nums):
    count = 0
    for i in nums:
        if is_prime(i) == True:
            count += 1

    print(count)


count_prime(input_val)




