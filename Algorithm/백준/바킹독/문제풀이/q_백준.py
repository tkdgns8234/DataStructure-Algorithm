# 1. 큐
# from collections import deque
# import sys
# input = sys.stdin.readline
# n = int(input())
# q = deque()
# for i in range(n):
#     command = input().split()
#     if command[0] == 'push':
#         q.append(int(command[1]))
#     elif command[0] == 'pop':
#         print(-1) if not q else print(q.popleft())
#     elif command[0] == 'size':
#         print(len(q))
#     elif command[0] == 'empty':
#         print(0) if q else print(1)
#     elif command[0] == 'front':
#         print(q[0]) if q else print(-1)
#     elif command[0] == 'back':
#         print(q[-1]) if q else print(-1)

# 2. 카드2
# from collections import deque
# n = int(input())
# data = deque([i for i in range(1, n + 1)])
# while len(data) > 1:
#     data.popleft()
#     data.append(data.popleft())
#
# print(data[0])

# 3. 회전하는 큐
# from collections import deque
# n, m = map(int, input().split())
# data = deque([i for i in range(1, n + 1)])
# target = list(map(int, input().split()))
#
# def move_left():
#     global data
#     data.append(data.popleft())
#
# def move_right():
#     global data
#     data.appendleft(data.pop())
#
# count = 0
# for i in target:
#     while True:
#         if i == data[0]:
#             data.popleft()
#             break
#         else:
#             now = data.index(i)
#             if now < len(data) - now:
#                 move_left()
#                 count += 1
#             else:
#                 move_right()
#                 count += 1
# print(count)

# 4. AC
# 실제로 배열을 뒤집으면 절대 시간내로 해결할 수 없다 (뒤집는것의 시간복잡도가 O(n) 이기 때문에)
# 뒤집은것같은 효과를 내야한다 양방향 큐로
# 잘 했는데 문제가 몇가지 있었다
# 배열 받은거 int형 변환이 필요 없음에도 습관적으로 map(int, 로 변환시킨 문제
# string 연산 중 strip 말고 [::] 연산으로 앞뒤원소제거가능
# 출력으로 원하는 print form 을 제대로 보자.. ex)) [1, 2, 3, 4] 가아니라 [1,2,3,4] 였다


# from collections import deque
# T = int(input())
#
# for i in range(T):
#     p = list(input())
#     n = int(input())
#     num_list = deque(input().strip('['']').split(','))
#
#     left = True
#     error = False
#     for action in p:
#         if action == 'R':
#             left = not left
#         elif action == 'D':
#             if not num_list or n == 0:
#                 error = True
#                 break
#
#             if left:
#                 num_list.popleft()
#             else:
#                 num_list.pop()
#     if error:
#         print('error')
#         continue
#     if not left:
#         num_list.reverse()
#     print('[', ','.join(num_list), ']', sep="")
