
# su = '123333214'
# l = list(su)

# print(l)

# arr = [1,2,3,4,5,6]
# for i in range(len(arr)-1,-1, -1):
#     print(arr[i])
#
# arr = [1,2,3,4]
# print(arr[0:-2])

# p = [(1, 2), (3, 1), (2, 3)]
#
# print(p[2][1])
# s = ['a','b','c','d']
# count = 1
# s = 2
# print(count if s == 1 else count)

# arr = [[-1] * 2 for i in range(5)]
# print(arr)

# result = -4
# result //= 3
#
# print(result)
# result2 = -4
# print(int(result2 / 3))

# from itertools import permutations
# oper = ['+','+','-']
#
# print(list(permutations(oper, 3)))
#

# pos = {(1, 2), (2, 1)}
# pos2 = {(2, 1), (1, 2)}
# l = []
# l.append(pos)
# l.append(pos2)
#
# print(l)

# print(list(pos))

# print(0/3)

# vertices = [[1, 7, 12], [4, 7, 13], [1, 5, 17], [3, 5, 20], [2, 4, 24], [
#     1, 4, 28], [3, 6, 37], [5, 6, 45], [2, 5, 62], [1, 2, 67], [5, 7, 73]]
#
# numvert = map(max, vertices)
#
# print(numvert)

# from itertools import combinations
# l = [1, 2, 3, 4]
# print(list(combinations(l, 3)))

# l = [1,2,3,4]
# l += [1,1,1]
# data =[1,2,3,4]
# print(range(len(data)-1, -1, -1))

# test = []
# test.insert(3, 3)
# test.insert(2, 2)
# print(list(reversed(test)))
#
# def bfs():
#     while fire_q:
#         x, y = fire_q.popleft()
#         for move in move_type:
#             nx, ny = x+move[0], y+move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if data[nx][ny] == '#' or dist_fire[nx][ny] > 0:
#                 continue
#             dist_fire[nx][ny] = dist_fire[x][y] + 1
#             fire_q.append((nx,ny))
#
#     while jh_q:
#         x, y = jh_q.popleft()
#         for move in move_type:
#             nx, ny = x+move[0], y+move[1]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 return dist_jh[x][y] + 1
#             if data[nx][ny] == '#' or dist_jh[nx][ny] > 0:
#                 continue
#             if dist_fire[nx][ny] == 0 or dist_fire[nx][ny] > dist_jh[x][y] + 1:
#                 jh_q.append((nx,ny))
#                 dist_jh[nx][ny] = dist_jh[x][y] + 1
#     return 'IMPOSSIBLE'
# import sys
# input = sys.stdin.readline
# a = list(map(int, list(input().split())))
# print(a)
# import sys
# input = sys.stdin.readline
#
# k = int(input())
# m, n = map(int, input().split())
# print(m, n)
# data = [list(map(int, input().split())) for _ in range(n)]
# print(data)

# array = [[] for i in range(5)]
#
# for i in range(5):
#     for j in range(1, 9):
#         array[i].append(j + 8 * i)
#
# print(*array, sep='\n')
#
# n = 2
# m = 3
#
# for i in range(5 - n):
#     for j in range(8 - m):
#         sample_matrix = [row[j:j + 3] for row in array[i:i + 2]]
#         print(*sample_matrix, sep='\n')
#         print()

# 2차원배열 slice
# data = [list(map(int, input().split())) for _ in range(9)]
# length= 9
#
# for i in range(0, length, length // 3):
#     for j in range(0, length, length // 3):
#         print(*[row[j:j + length // 3] for row in data[i:i + length // 3]], sep="\n")
#         print()

# 배열
# test = []
# test.append([])
# test[-1].append(111)
# test.append([])
# test[-1].append(222)
# print(test)
#
# data = [[1,2,3,4,5], [6,7,8,9,10]]
# data[0][1:3] = [0,0]
# print(data)

# data = [1,2,3,4,5,6]
# data[0:5] = [0,0,0,0,0]
# print(data)

# 5. 별 찍기 - 10
# 아래 방법 좋은데, 배열이 너무많아져 4차원,6차원... 값을 어떻게 찍을지도 문제다
# 풀이를 찾아보자..
# 아래 코드는 실패
# def reculsive(num):
#     if num == 1:
#         return '*'
#     priv = reculsive(num//3)
#     arr = []
#
#     for i in range(3):
#         for j in range(3):
#             if num//3 <= i < num//3*2:
#                 if num//3 <= j < num//3*2:
#                     arr.append(' ')
#                     continue
#             arr.append(priv)
#     return arr
#
# n = int(input()) # 3
# print(reculsive(n))
# print('\n'.join(reculsive(n)))
# # rs = reculsive(n)

# from sys import stdin
#
# input = stdin.readline
#
# dr = (-1, 1, 0, 0)
# dc = (0, 0, -1, 1)
#
#
# def check(num):
#     global available
#     r = num // 5
#     c = num % 5
#     for d in range(4):
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
#             continue
#         nextNum = nr * 5 + nc  # 다음 숫자
#         if nextNum in p:  # p에 있다면 방문표시, 재귀로 다음 숫자 넘겨 재검사
#             visited[nr][nc] = 1
#             available += 1
#             check(nextNum)
#
#
# # (depth, Y의 갯수, 사용할 숫자 인덱스)
# def dfs(depth, ycnt, idx):
#     global result, available, visited
#     if ycnt > 3 or 25 - idx < 7 - depth:  # 가지치기
#         return
#
#     if depth == 7:  # depth가 7에 도달하면 연결 여부 검사
#         available = 1  # 연결된 좌표 갯수
#         visited = [[0] * 5 for _ in range(5)]
#         sr, sc = p[0] // 5, p[0] % 5  # 5*5 맵 좌표로 변환
#         visited[sr][sc] = 1  # 시작 위치 표시
#         check(p[0])  # 연결된 좌표인지 확인
#         if available == 7:  # 7개 좌표가 연결됐다면 +1
#             result += 1
#         return
#
#     # 5*5 맵 좌표로 변환
#     r = idx // 5
#     c = idx % 5
#
#     if A[r][c] == "Y":  # "Y"이면 ycnt +1
#         p.append(idx)
#         dfs(depth + 1, ycnt + 1, idx + 1)
#         p.pop()
#     else:  # "S"이면 그냥 넘기기
#         p.append(idx)
#         dfs(depth + 1, ycnt, idx + 1)
#         p.pop()
#     dfs(depth, ycnt, idx + 1)  # 꼭 필요한 코드. 사용하지 않고, 그냥 인덱스만 넘긴다!
#
#
# # main
# A = [input().rstrip() for _ in range(5)]
# result = 0
# p = []
# dfs(0, 0, 0)
# print(result)

# from collections import deque
# data = [1,23,4]
# q = deque([data])
# a, b, c = q.popleft()
# print(a,b,c)

# # 배열 얕은복사 test
# def rotate(k):
#     result = [1,k]
#     data[k] = result
#     return
#
#
# data = [[1,2],[3,4], [5,6]]
# rotate(0)
# rotate(1)
# rotate(2)
# data[0][0] = -1
# print(data)



# 블로그 풀이
from sys import stdin
from itertools import permutations
from collections import deque

# input = stdin.readline
# dx = [-1,1,0,0,0,0]
# dy = [0,0,-1,1,0,0]
# dz = [0,0,0,0,-1,1]
# INF = 9876543210
#
# board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
# visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
# visited_num = 0
# answer = INF
#
# def solv():
#     for order in permutations(range(5),5):
#         stack_board(order,0)
#     print(answer if answer != INF else -1)
# def stack_board(order,idx):
#     global board
#     if answer == 12:
#         return
#     if idx == 5:
#         simul(order)
#         return
#     for _ in range(4):
#         board_rotate(order[idx])
#         stack_board(order,idx+1)
#
# def simul(order):
#     global answer,visited,visited_num
#     game_board = []
#     for idx in order:
#         game_board.append(board[idx])
#
#     visited_num += 1
#
#     start = [0,0,0]
#     end = [4,4,4]
#
#     if game_board[start[0]][start[1]][start[2]] != 1 or game_board[end[0]][end[1]][end[2]] != 1:
#         return
#
#     visited_num += 1
#     q = deque([start+[0]])
#     visited[0][start[0]][start[1]] = visited_num
#     while q:
#         z,x,y,cnt = q.pop()
#
#         if cnt >= answer:
#             continue
#         if end[0] == z and end[1] == x and end[2] == y:
#             answer = min(answer,cnt)
#             break
#
#         for d in range(6):
#
#             nz = z + dz[d]
#             nx = x + dx[d]
#             ny = y + dy[d]
#
#             if point_validator(nz,nx,ny,game_board):
#                 visited[nz][nx][ny] = visited_num
#                 q.appendleft((nz,nx,ny,cnt+1))
#
# def point_validator(z,x,y,game_board):
#     if z < 0 or x < 0 or y < 0 or z >= 5 or x >= 5 or y >= 5:
#         return False
#     elif game_board[z][x][y] == 0:
#         return False
#     elif visited[z][x][y] == visited_num:
#         return False
#     return True
#
# def board_rotate(z):
#     global board
#
#     tmp = []
#     for row in board[z]:
#         tmp_row = []
#         for num in row:
#             tmp_row.append(num)
#         tmp.append(tmp_row)
#
#     for x in range(5):
#         for y in range(5):
#             board[z][y][4-x] = tmp[x][y]
#
# solv()

# n, m = 2, 2
# visited = [[[[False] * m for _ in range(n)] * m] for _ in range(n)]
# visited2 = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
#
# visited2[1][1][1][1] = 1
# print(visited)
# print()
# print(visited2)

# a = [[0],[1]]
# b = a*3
# b[0][0] = 1
# print(a)

# test = [1,2,3,4,5]
# print(sum(test))
# test = [1,2,3,4,5]
# for i in range(len(test)-1, -1, -2):
#     print(test[i])

# import sys
# input = sys.stdin.readline
#
# data = list(input().split())
# print(data)


# import sys
# from collections import Counter
#
# n = int(sys.stdin.readline())  # 학생 수
# arr = list(map(int, sys.stdin.readline().split()))  # 학생 코딩 실력
# arr.sort()
# cnt_ = Counter(arr)  # 해당 점수에 해당하는 학생 수 얻기
# result = 0
# # 학생을 한명 씩 돌린다.
# for i, a in enumerate(arr):
#     left, right = i + 1, n - 1
#     while left < right:
#         sum_ = arr[left] + arr[right] + arr[i]
#         # 1. 점수 총합이 0인 경우, 같은 값이 있는 것에 대한 처리 필요
#         if sum_ == 0:
#             #  left값과 right 갑이 같은 경우 해당 범위 저장. -4 2 2 2 2
#             if arr[left] == arr[right]:
#                 result += right - left
#             # 다른 경우 right 값에 대한 개수 합 -4 1 1 1 3 3 3
#             else:
#                 result += cnt_[arr[right]]
#             left += 1
#         # 2. 점수 총합이 0 보다 큰 경우
#         elif sum_ > 0:
#             right -= 1
#         # 3. 점수 총합이 0 보다 작은 경우
#         elif sum_ < 0:
#             left += 1
#
# print(result)

dict = {1:1}
if dict[2]:
    print(0)
else:
    print(1)