# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

input_val = input().upper()

def find_max_alp(strs):
    uniq = []
    for i in range(len(strs)): # 문자열 길이만큼 반복
        if strs[i] not in uniq: # 유니크 문자열 탐색
            uniq.append(strs[i])
    
    count_s = 0
    for j in uniq:
        temp_count = strs.count(j)
        temp_str = j

        if temp_count > count_s:
            count_s = temp_count
            final_s = j
        elif temp_count == count_s:
            final_s = "?"
        
    print(final_s)


find_max_alp(input_val)