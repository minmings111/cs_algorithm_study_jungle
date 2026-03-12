# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

case_count = int(input())
data_list = []

for i in range(case_count):
    temp_data = list(map(int, input().split()))
    data_list.append(temp_data)


def tell_the_truth(case):
    n = case[0]
    scores = case[1:]
    avg = sum(scores)/n
    count_n = 0

    for i in range(n):
        if scores[i] > avg:
            count_n += 1
    
    per = round(count_n/n*100, 3)
    print(f"{per}%")

for i in range(0,case_count):
    tell_the_truth(data_list[i])

    