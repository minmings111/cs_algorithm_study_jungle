# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

input_val = int(input())

s_str = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
q_srt = '"재귀함수가 뭔가요?"'
a_str1_1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
a_str1_2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
a_str1_3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

a_str2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'

e_str = "라고 답변하였지."

# 

def repeat(num):
    
    print("____"*(input_val-num)+q_srt)

    if num > 0:
        print("____"*(input_val-num)+a_str1_1)
        print("____"*(input_val-num)+a_str1_2)
        print("____"*(input_val-num)+a_str1_3)
        repeat(num-1)
    else:
        print("____"*(input_val-num)+a_str2)


    print("____"*(input_val-num)+ e_str)


print(s_str)
repeat(input_val)


