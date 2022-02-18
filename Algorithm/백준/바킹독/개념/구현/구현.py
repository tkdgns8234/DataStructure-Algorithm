# 문제 1. 주사위 굴리기
# 복잡하게 생각하면 끝도없이 복잡해지는 문제다.
# 키워드는 주사위를 1차원 배열공간에 임의로 설정 해 놓는것
# 방향: index   ex) 바닥: 0 동: 1 서: 2 ....

# n, m, x, y, k = map(int, input().split())
#
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#
# moves = list(map(int, input().split()))
#
# # 주사위 인덱스
# # 바닥 동 서 남 북 윗면
# # 0   1  2 3 4  5
# j = [0 for i in range(6)]
#
# # 동 서 남 북
# move_type = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]
#
# # x,y 는 현재 지도상 위치
# for move in moves:
#     nx = x + move_type[move][0]
#     ny = y + move_type[move][1]
#
#     if nx < 0 or ny < 0 or nx >= n or ny >= m:
#         continue
#
#     if move == 1: # 동쪽
#         j[0], j[1], j[2], j[5] = j[1], j[5], j[0], j[2]
#     elif move == 2: # 서쪽
#         j[0], j[1], j[2], j[5] = j[2], j[0], j[5], j[1]
#     elif move == 3: # 남쪽
#         j[0], j[3], j[4], j[5] = j[3], j[5], j[0], j[4]
#     elif move == 4: # 북쪽
#         j[0], j[3], j[4], j[5] = j[4], j[0], j[5], j[3]
#
#     if data[nx][ny] == 0:
#         data[nx][ny] = j[0]
#     else:
#         j[0] = data[nx][ny]
#         data[nx][ny] = 0
#
#     x, y = nx, ny
#     print(j[5])

# 문제 2. 그룹 단어 체커
# 지문을 잘 읽고 그대로 표현하면 풀 수 있다.
# n = int(input())
# count = 0
# for _ in range(n):
#     result = True
#     word = input()
#     for i in range(0, len(word) - 1):
#         if word[i] != word[i + 1]:
#             if word[i] in word[i + 1:]:
#                 result = False
#     if result:
#         count += 1
# print(count)

# 문제3 셀프 넘버
# 셀프넘버가 아닌것 추가
# def d(n):
#     n = n + sum(map(int, str(n)))
#     return n
#
# not_self_num = []
# for i in range(1, 10001):
#     not_self_num.append(d(i))
#
# for i in range(1, 10001):
#     if i not in not_self_num:
#         print(i)

# 문제4 프린터 큐
# 너무 억지스럽게 풀었어.. 다시풀자
# 리스트 활용법만 알면 굳이 queue 쓰지 않아도 돼

# from collections import deque
# for test in range(int(input())):
#     n, target = map(int, input().split())
#     imp = list(map(int, input().split()))
#
#     data = []
#     for i in range(n):
#         data.append(((imp[i]), i))
#     data = deque(data)
#
#     cnt = 1
#     while True:
#         is_moved = False
#         for i in range(1, n):
#             if data[0][0] < data[i][0]:
#                 val = data.popleft()
#                 data.append(val)
#                 is_moved = True
#                 break
#
#         if not is_moved:
#             val = data.popleft()
#             if val[1] == target:
#                 print(cnt)
#                 break
#             cnt += 1
#             n -= 1

# 프린터 큐
# for test in range(int(input())):
#     n, target = map(int, input().split())
#     imp = list(map(int, input().split()))
#     target_list = [0 for i in range(n)]
#     target_list[target] = 1
#
#     cnt = 1
#     while True:
#         if imp[0] == max(imp):
#             if target_list[0] == 1:
#                 print(cnt)
#                 break
#             else:
#                 imp.pop(0)
#                 target_list.pop(0)
#             cnt += 1
#         else:
#             imp.append(imp[0])
#             target_list.append(target_list[0])
#             imp.pop(0)
#             target_list.pop(0)

# 문제 5 아기 상어
# 와,, 이거 bfs 특성을 잘 이해하고 있으면 좀 더 간단하게 풀 수 있어
# 어려워서 문제 푸는 중 블로그를 한 번 봤다.
# 계속 참고하면서 했어.. 연습 계속 해야겠다
# flag 를 통해 물고기를 찾은 경우, 찾은 시간까지는 탐색을 모두 완료시켜서
# 물고기를 전부 담고, 문제에서 요구하는 물고기 먼저먹는 순서대로 먹은 후 다시 bfs를 돌리는 형식
# 그리고 bfs 할 때 함수 말고 while 문으로 바로 돌리는게 코드가 더 깔끔하다

# from collections import deque
# def bfs(start, space):
#     # 최단거리의 먹이 위치 찾고 먹으면서 초 세기, 상어 크기 키우기
#     sx, sy = start
#     shark_size = 2
#     eat = 0
#     move_num = 0
#
#     while True:
#         q = deque()
#         q.append((sx, sy, 0))
#         visited = [[False] * n for _ in range(n)]
#         visited[sx][sy] = True
#         flag = int(1e9)
#         fish = []
#         while q:
#             x, y, second = q.popleft()
#             if second > flag:
#                 break
#             for move in move_type:
#                 nx, ny = x + move[0], y + move[1]
#                 if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                     continue
#                 if shark_size < space[nx][ny] or visited[nx][ny]:
#                     continue
#
#                 if shark_size > space[nx][ny] != 0:
#                     flag = second
#                     fish.append((nx, ny, second + 1))
#                 q.append((nx, ny, second + 1))
#                 visited[nx][ny] = True
#
#         if len(fish) > 0:
#             fish.sort()
#             x, y, second = fish[0]
#             move_num += second
#             eat += 1
#             space[x][y] = 0
#             if eat == shark_size:
#                 shark_size += 1
#                 eat = 0
#             sx, sy = x, y
#         else:
#             print(move_num)
#             break
#
# n = int(input())
#
# space = []
# for i in range(n):
#     space.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if space[i][j] == 9:
#             space[i][j] = 0
#             start = (i, j)
#
# move_type = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# bfs(start, space)

# 문제 6 테트로미노
