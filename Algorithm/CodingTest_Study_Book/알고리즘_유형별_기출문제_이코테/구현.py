# Q07 럭키 스트레이트

# n = list(map(int, input()))
# print(n)
# half = len(n) // 2
#
# left = n[0:half]
# right = n[half:]
#
# if sum(left) == sum(right):
#     print('LUCKY')
# else:
#     print('READY')

# Q08 문자열 재정렬
# s = input()
# str_list = []
# result = 0
# for i in s:
#     if i.isalpha():
#         str_list.append(i)
#     else:
#         result += int(i)
#
# str_list.sort()
#
# if result != 0:
#     str_list.append(str(result))
#
# print(''.join(str_list))

# Q09 문자열 압축
# def solution(s):
#     answer = len(s)
#
#     for step in range(1, len(s) // 2 + 1):
#         prev = s[0:step]
#         count = 1
#         result = ""
#         for j in range(step, len(s), step):
#             if prev == s[j:j+step]: # j+step 을 해도 값이 len(s)를 넘어가지 않는다
#                 count += 1
#             else:
#                 result += str(count) + prev if count >= 2 else prev
#                 prev = s[j:j+step]
#                 count = 1
#         result += str(count) + prev if count >= 2 else prev
#
#         answer = min(answer, len(result))
#     return answer

# Q10 자물쇠와 열쇠

# 90도 회전
# def rotation(key):
#     col = len(key)
#     row = len(key[0])
#     new_key = [[0]*col for _ in range(row)]
#     for i in range(row):
#         for j in range(col):
#             new_key[j][row-i-1] = key[i][j]
#     return new_key
#
# def is_correct(new_lock):
#     length = len(new_lock)
#     for i in range(length//3, length-length//3):
#         for j in range(length // 3, length - length // 3):
#             if new_lock[i][j] != 1:
#                 return False
#     return True
#
#
# def solution(key, lock):
#     n = len(key)
#     m = len(lock)
#     new_lock = [[0]*(m*3) for _ in range(m*3)]
#     # new_lock 초기화
#     for i in range(m):
#         for j in range(m):
#             new_lock[i+m][j+m] = lock[i][j]
#
#     # 회전4번
#     for _ in range(4):
#         key = rotation(key)
#
#         # key 이동
#         for i in range(m*2):
#             for j in range(m*2):
#                 # key 대입
#                 for a in range(n):
#                     for b in range(n):
#                        new_lock[i+a][j+b] += key[a][b]
#
#                 if is_correct(new_lock):
#                     return True
#                 # key 빼기
#                 for a in range(n):
#                     for b in range(n):
#                        new_lock[i+a][j+b] -= key[a][b]
#     return False

# Q11 뱀
#방향 전환 상수
# LEFT = 'L'
# RIGHT = 'D'
#
# # left, right, up, down
# side_type = ['U','R','D','L']
# move_type = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#
# # 보드의 크기
# n = int(input())
# # 사과의 갯수
# k = int(input())
#
# graph = [[0] * (n+1) for i in range(n+1)]
#
# # 0 은 맵
# # 1 은 뱀의 몸통
# # 사과는 3으로 지정
# for _ in range(k):
#     x, y = map(int, input().split())
#     graph[x][y] = 3
#
# # 방향전환 횟수
# rotation = []
# L = int(input())
# for i in range(L):
#     l = input().split()
#     rotation.append((int(l[0]), l[1]))
#
# def rotation_left_right(type, side):
#     result = 0
#     now = side_type.index(side)
#     if type == RIGHT:
#         if now < 3:
#             result = now + 1
#         else:
#             result = 0
#     else:
#         if now == 0:
#             result = 3
#         else:
#             result = now - 1
#     return side_type[result]
#
# x = y = 1
# graph[x][y] = 1
# time = 0
# side = side_type[1]
#
# tail_position = 0
# remember_move = []
# remember_move.append((x, y))
#
# while True:
#     for i in rotation:
#         if i[0] == time:
#             side = rotation_left_right(i[1], side)
#
#     for i in range(len(side_type)):
#         if side == side_type[i]:
#             nx = x + move_type[i][0]
#             ny = y + move_type[i][1]
#
#     if nx < 1 or ny < 1 or nx >= len(graph) or ny >= len(graph):
#         time += 1
#         break
#     if graph[nx][ny] == 1:
#         time += 1
#         break
#     # 사과가 아닌 경우
#     if graph[nx][ny] != 3:
#         # 꼬리 자르기
#         tail_x, tail_y = remember_move[tail_position]
#         graph[tail_x][tail_y] = 0
#         # 꼬리 이동
#         tail_position += 1
#
#     graph[nx][ny] = 1
#     x, y = nx, ny
#     remember_move.append((x, y))
#     time += 1
#
# print(time)
#


