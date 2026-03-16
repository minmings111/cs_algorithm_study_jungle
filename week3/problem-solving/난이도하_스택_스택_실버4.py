# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

n = int(input())
stack = [input().split() for i in range(n)]

def user_command(input_command):
    num_stack = []
    for i in input_command:
        command = i[0]

        if command in "push":
            value = i[1]
            num_stack.append(value)

        elif command in "pop":
            if num_stack:
                temp = num_stack.pop()
                print(temp)
            else:
                print("-1")
        
        elif command in "size":
            print(len(num_stack))
        
        elif command in "empty":
            if num_stack:
                print("0")
            else:
                print("1")
        
        elif command in "top":
            if num_stack:
                print(num_stack[-1])
            else:
                print("-1")
    
user_command(stack)


