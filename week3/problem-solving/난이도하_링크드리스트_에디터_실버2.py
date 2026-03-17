# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

# 시간 초과로 제출할 수 없는 코드...
first_strs = input()
n = int(input())
n_list = [input() for i in range(n)]

class node():
    def __init__(self, data):
        self.data = data
        self.before = None
        self.next = None

def init_set(input_list):
    first_node = None

    for i in input_list:
        if first_node == None:
            first_node = node(i)
            prev = first_node   
        else:
            temp_node = node(i)
            temp_node.before = prev
            prev.next = temp_node
            prev = temp_node

    end_node = node("end")
    end_node.before = prev
    prev.next = end_node   
    return first_node, end_node

fir_node, last_node = init_set(first_strs)

def command_order(f_node, e_node, command_list):
    cursor_point = e_node
    for command in command_list:
        if cursor_point != f_node and command == "L":
            cursor_point = cursor_point.before
        elif cursor_point != e_node and command == "D":
            cursor_point = cursor_point.next
        elif cursor_point != f_node and command == "B":
            if cursor_point.before.before != None:
                now_bef = cursor_point.before.before
                now_bef.next = cursor_point
                cursor_point.before = now_bef
            else:
                cursor_point.before = None
                f_node = cursor_point      
        elif command[0] == "P":
            temp_n = command[-1]
            if cursor_point.before != None:  
                add_node = node(temp_n)
                add_node.next = cursor_point
                add_node.before = cursor_point.before
                cb_node= cursor_point.before
                cb_node.next = add_node
                cursor_point.before = add_node
            else:
                add_node = node(temp_n)
                add_node.next = cursor_point
                cursor_point.before = add_node
                f_node = add_node
    return f_node, e_node

fir_node, last_node = command_order(fir_node, last_node, n_list)

cur_nod = fir_node
while cur_nod != last_node:
    print(cur_nod.data, end="")
    cur_nod = cur_nod.next
print()

# 참고해볼 코드..!
# import sys
# from collections import deque

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.prev = None
#         self.next = None

# def solution():
#     data = sys.stdin.read().split()
#     if not data: 
#          return
    
#     text = data[0]
#     commands = data[2:]

#     head, tail = Node(), Node()
#     cursor = [tail]

#     def link(a, b):
#         a.next, b.prev = b, a

#     def move(to):
#         cursor[0] = to

#     link(head, tail)

#     ops = {
#         "L": lambda: move(cursor[0].prev) if cursor[0].prev != head else None,
#         "D": lambda: move(cursor[0].next) if cursor[0] != tail else None,
#         "B": lambda: link(cursor[0].prev.prev, cursor[0]) if cursor[0].prev != head else None,
#         "P": lambda x: (new := Node(x), link(cursor[0].prev, new), link(new, cursor[0]))
#     }

#     for char in text:
#         ops["P"](char)

#     curr = 0
#     while curr < len(commands):
#         cmd = commands[curr]

#         if cmd == "P":
#             ops["P"](commands[curr + 1])
#             curr += 2
#         else:
#             ops[cmd]()
#             curr += 1

#     result, node = [], head.next
#     while node != tail:
#         result.append(node.data)
#         node = node.next

#     sys.stdout.write("".join(result) + "\n")

# if __name__ == "__main__":
#     solution()
