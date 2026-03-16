# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque

input_val = int(input())

def find_final_card(input_num):
    card_queue = deque(range(1, input_num+1))

    while len(card_queue) > 1:
        card_queue.popleft()
        temp = card_queue.popleft()
        card_queue.append(temp)
    
    print(card_queue.popleft())
    return

find_final_card(input_val)