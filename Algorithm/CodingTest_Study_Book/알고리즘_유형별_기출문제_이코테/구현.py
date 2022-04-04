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

# Q12 기둥과 보 설치
# def condition(answer):
#     for ans in answer:
#         x, y, what = ans
#         # 기둥
#         if what == 0:
#             if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
#                 continue
#             return False
#         # 보
#         elif what == 1:
#             if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or [x-1, y, 1] in answer and [x+1, y, 1] in answer:
#                 continue
#             return False
#     return True
#
#
# def solution(n, build_frame):
#     answer = []
#     for frame in build_frame:
#         # x, y, 기둥/보, 삭제/설치
#         x, y, what, action = frame
#         # 삭제
#         if action == 0:
#             answer.remove([x, y, what])
#             if not condition(answer):
#                 answer.append([x, y, what])
#         # 설치
#         elif action == 1:
#             answer.append([x, y, what])
#             if not condition(answer):
#                 answer.remove([x, y, what])
#     answer.sort()
#     return answer

# Q13 치킨 배달
# 다시 풀어야함
# 어떻게 구현하면 좋을지 적절한 방법을 좀 더 생각한 후에 구현을 시작하자 꼭
# 아래 코드는 완전히 잘못 접근했다
# 너무 최단거리라는 말에 집중해서 강제로 bfs를 적용하려다가 망했다
# 문제에서 주어지는 설명에 조금 더 집중해서 구현하면 좋겠다

# ------------------------------------
# from collections import deque
# import copy
# def bfs(arr, start):
#     c_arr = copy.deepcopy(arr)
#     x, y = start
#     q = deque()
#     q.append((x, y))
#     # 3인경우 방문
#     c_arr[x][y] = 3
#     while q:
#         x, y = q.popleft()
#         if c_arr[x][y] == CHICKEN_STORE:
#             # 가장 가까운 거리의 치킨집 x,y 좌표 리턴
#             return tuple(x,y)
#
#         if c_arr[x][y] != 3:
#             q.append((x + 1, y))
#             q.append((x - 1, y))
#             q.append((x, y + 1))
#             q.append((x, y - 1))
#     # 찾을 수 없는경우
#     return None
#
# EMPTY = 0
# HOUSE = 1
# CHICKEN_STORE = 2
#
# n, m = map(int, input().split())
#
# arr = []
# # 가까운 거리의 집의 갯수 (x,y,갯수)
# chicken_house_count = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == HOUSE:
#             if bfs(arr, (i, j)) is not None:
#                 # 가까운 치킨집의 x, y 좌표
#                 x, y = bfs(arr, (i, j))
#                 chicken_house_count[x][y] += 1
#
# distance = []
# for i in range(n):
#     for j in range(n):
#         if chicken_house_count[i][j] != 0:
#             distance.append(chicken_house_count[i][j], i, j)
#
# distance.sort()
# for _ in range(len(distance) - (len(distance) - m)):
#     val = distance.pop()
#     dis, x, y = val
#     arr[x][y] = 0
# ------------------------------------

# Q14 외벽 점검
# 다시풀자
# 원형문제의 경우 길이를 두배로 해서 일자로 표현한 후 푸는게 좋다
# 주어진 숫자가 매우 적으니 완전탐색

# def solution(n, weak, dist):
#
#     answer = 0
#     return answer

# 다시 풀기
import itertools
def solution(n, weak, dist):
    length = len(weak)
    # 1. weak 배열의 길이를 2배로 늘리기
    for i in range(length):
        weak.append(weak[i]+n)
    # 2. 투입할 친구의 최솟값을 찾기 위해 최댓값보다 1 큰 값으로 초기화
    answer = len(dist)+1
    # 3. 0부터 length-1까지 start 이동하면서 찾기
    for start in range(length):
        for friends in list(itertools.permutations(dist, len(dist))):
            count = 1 # 투입할 친구 수
            # 현재 친구가 점검 가능한 위치 구하기
            position = weak[start]+friends[count-1]
            # 시작점 부터 모든 취약지점 확인
            for i in range(start, start+length):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i]+friends[count-1]

            answer = min(count, answer)

    if answer > len(dist):
        return -1
    return answer

a = solution(12, [1,3,6,10], [1,1,1])
print(a)