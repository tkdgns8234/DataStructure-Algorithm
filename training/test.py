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

# 2???????????? slice
# data = [list(map(int, input().split())) for _ in range(9)]
# length= 9
#
# for i in range(0, length, length // 3):
#     for j in range(0, length, length // 3):
#         print(*[row[j:j + length // 3] for row in data[i:i + length // 3]], sep="\n")
#         print()

# ??????
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

# 5. ??? ?????? - 10
# ?????? ?????? ?????????, ????????? ??????????????? 4??????,6??????... ?????? ????????? ???????????? ?????????
# ????????? ????????????..
# ?????? ????????? ??????
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
#         nextNum = nr * 5 + nc  # ?????? ??????
#         if nextNum in p:  # p??? ????????? ????????????, ????????? ?????? ?????? ?????? ?????????
#             visited[nr][nc] = 1
#             available += 1
#             check(nextNum)
#
#
# # (depth, Y??? ??????, ????????? ?????? ?????????)
# def dfs(depth, ycnt, idx):
#     global result, available, visited
#     if ycnt > 3 or 25 - idx < 7 - depth:  # ????????????
#         return
#
#     if depth == 7:  # depth??? 7??? ???????????? ?????? ?????? ??????
#         available = 1  # ????????? ?????? ??????
#         visited = [[0] * 5 for _ in range(5)]
#         sr, sc = p[0] // 5, p[0] % 5  # 5*5 ??? ????????? ??????
#         visited[sr][sc] = 1  # ?????? ?????? ??????
#         check(p[0])  # ????????? ???????????? ??????
#         if available == 7:  # 7??? ????????? ??????????????? +1
#             result += 1
#         return
#
#     # 5*5 ??? ????????? ??????
#     r = idx // 5
#     c = idx % 5
#
#     if A[r][c] == "Y":  # "Y"?????? ycnt +1
#         p.append(idx)
#         dfs(depth + 1, ycnt + 1, idx + 1)
#         p.pop()
#     else:  # "S"?????? ?????? ?????????
#         p.append(idx)
#         dfs(depth + 1, ycnt, idx + 1)
#         p.pop()
#     dfs(depth, ycnt, idx + 1)  # ??? ????????? ??????. ???????????? ??????, ?????? ???????????? ?????????!
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

# # ?????? ???????????? test
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


# ????????? ??????
import heapq
import math
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
# n = int(sys.stdin.readline())  # ?????? ???
# arr = list(map(int, sys.stdin.readline().split()))  # ?????? ?????? ??????
# arr.sort()
# cnt_ = Counter(arr)  # ?????? ????????? ???????????? ?????? ??? ??????
# result = 0
# # ????????? ?????? ??? ?????????.
# for i, a in enumerate(arr):
#     left, right = i + 1, n - 1
#     while left < right:
#         sum_ = arr[left] + arr[right] + arr[i]
#         # 1. ?????? ????????? 0??? ??????, ?????? ?????? ?????? ?????? ?????? ?????? ??????
#         if sum_ == 0:
#             #  left?????? right ?????? ?????? ?????? ?????? ?????? ??????. -4 2 2 2 2
#             if arr[left] == arr[right]:
#                 result += right - left
#             # ?????? ?????? right ?????? ?????? ?????? ??? -4 1 1 1 3 3 3
#             else:
#                 result += cnt_[arr[right]]
#             left += 1
#         # 2. ?????? ????????? 0 ?????? ??? ??????
#         elif sum_ > 0:
#             right -= 1
#         # 3. ?????? ????????? 0 ?????? ?????? ??????
#         elif sum_ < 0:
#             left += 1
#
# print(result)

# dict = {1:1}
# if dict[2]:
#     print(0)
# else:
#     print(1)

# dic = dict()
# dic['a'] = 'a'
# print(dic)
# def solution(N, stages):
#     answer = []
#     fail = []
#     info = [0] * (N + 2)
#     for stage in stages:
#         info[stage] += 1
#     for i in range(N):
#         be = sum(info[(i + 1):])
#         yet = info[i + 1]
#         if be == 0:
#             fail.append((str(i + 1), 0))
#         else:
#             fail.append((str(i + 1), yet / be))
#     for item in sorted(fail, key=lambda x: x[1], reverse=True):
#         answer.append(int(item[0]))
#     return answer
#
# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
#
# test = [1,2,3,4]
# print(list(reversed(test)))
# t = bin(9)[2:]
# t = str(t).rjust(11, '0')
# print(t)
# s = 'serser'
# s[3] = 'b'-
# ss =[1,222,3]
# print(ss[1:2])
#
# from collections import deque
# def bfs(start, space):
#     # ??????????????? ?????? ?????? ?????? ???????????? ??? ??????, ?????? ?????? ?????????
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
#             print(x, y)
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
#
# def Binary_Search_Upper(data_list, x):                  #????????? list?????? x?????? ??? ???????????? ????????? ??????; log n ?????? ??????
#     left = 0
#     right = len(data_list) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if data_list[mid] <= x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return len(data_list) - (right + 1)
#
# v = Binary_Search_Upper([1,2,3,3,3,5], 3)
# print(v)
#
# from itertools import permutations
# print(len(list(permutations([1,2,3,4,5,6,7,8], 8))))
# import math
# print(math.factorial(8)/math.factorial(math.factorial(8)-math.factorial(8)))
# print(math.factorial(8))
# print(math.factorial(0))

# from itertools import permutations
#
# _list = [1, 2, 3, 4]
# perm = list(permutations(_list, 1))
# print(len(perm))

# import bisect
# test = [1,2,3,4]
# print(bisect.bisect_left(test, 2))
# print(bisect.bisect_right(test, 2))

# test = ['frodod', 'froddde', 'froddd']
# test.sort()
# print(test)
# n = int(input())
# t = []
# p = []
# dp = [0] * (n + 1)
#
# for i in range(n):
#     a, b = map(int, input().split())
#     t.append(a)
#     p.append(b)
#
# max_val = 0
# for i in range(n-1, -1, -1):
#     time = i + t[i]
#     if time <= n:
#         dp[i] = max(p[i] + dp[time], max_val)
#         max_val = dp[i]
#     else:
#         dp[i] = max_val
# print(max_val)

# def Binary_Search_Upper(data_list, x):                  #????????? list?????? x?????? ??? ???????????? ????????? ??????; log n ?????? ??????
#     left = 0
#     right = len(data_list) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if data_list[mid] <= x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return len(data_list) - (right + 1)
# 
# v = Binary_Search_Upper([1,2,3,3,3,5], 3)
# print(v)
#
# from collections import deque
# q = deque([(1,2,3,4)])
# now = q.popleft()
# print(now)

# print(-1%4)

# def test(a,b):
#     return a+b
#
# a =[1,2]
# print(test(*a))



# ?????? ??????
# import itertools
# def solution(n, weak, dist):
#     length = len(weak)
#     # 1. weak ????????? ????????? 2?????? ?????????
#     for i in range(length):
#         weak.append(weak[i]+n)
#     # 2. ????????? ????????? ???????????? ?????? ?????? ??????????????? 1 ??? ????????? ?????????
#     answer = len(dist)+1
#     # 3. 0?????? length-1?????? start ??????????????? ??????
#     for start in range(length):
#         for friends in list(itertools.permutations(dist, len(dist))):
#             count = 1 # ????????? ?????? ???
#             # ?????? ????????? ?????? ????????? ?????? ?????????
#             position = weak[start]+friends[count-1]
#             # ????????? ?????? ?????? ???????????? ??????
#             for i in range(start, start+length):
#                 if position < weak[i]:
#                     count += 1
#                     if count > len(dist):
#                         break
#                     position = weak[i]+friends[count-1]
#
#             answer = min(count, answer)
#
#     if answer > len(dist):
#         return -1
#     return answer
#
# a = solution(12, [1,3,6,10], [1,1,1])
# print(a)

# test = [1,4,3,2,52,6,4,7467,5,8,678]
# while test:
#     v = heapq.heappop(test)
#     print(v)



# # ??????????????? ??????????????? ?????? ????????? ????????? ??????
# import sys, heapq
# n = int(sys.stdin.readline())
# table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# check = [[[False] * 201 for _ in range(n)]for _ in range(n)]
# def bfs():
#     q = []
#     heapq.heappush(q, (0, table[0][0], table[0][0], 0, 0))
#     while q:
#         diff, temp_max, temp_min, x, y = heapq.heappop(q)
#         if x == n - 1 and y == n - 1:
#             return diff
#         if check[x][y][temp_min]:
#             continue
#         check[x][y][temp_min] = True
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 new_max = max(temp_max, table[nx][ny])
#                 new_min = min(temp_min, table[nx][ny])
#                 if check[nx][ny][new_min] == False:
#                     heapq.heappush(q, (new_max - new_min, new_max, new_min, nx, ny))
#
# print(bfs())

# from itertools import permutations

# def oper(a, b, op):
#     a, b = map(int, [a, b])
#     if op == '-':
#         return a-b
#     elif op == '*':
#         return a*b
#     elif op == '+':
#         return a+b

# def solve(op, exp):
#     # ????????? ?????????
#     arr = []
#     temp = ''
#     for e in exp:
#         if str(e).isnumeric():
#             temp += e
#         else:
#             arr.append(int(temp))
#             arr.append(e)
#             temp = ''
#     arr.append(int(temp))

#     for o in op:
#         stack = []
#         while arr:
#             v = arr.pop(0)
#             if v == o:
#                 stack.append(oper(stack.pop(), arr.pop(0), o))
#             else:
#                 stack.append(v)
#         arr = stack
#     return int(arr[0])


# def solution(expression):
#     answer = 0
#     for op in permutations(['+','*','-'], 3):
#         answer = max(answer, abs(solve(op, expression)))
#     return answer

# solution("100-200*300-500+20")

# ?????? ??? ?????????

# n, m = map(int, input().split())
# data = [int(input()) for i in range(n)]
# data.sort()
#
# ans = int(1e9)
# end = 0
# for start in range(n-1):
#     while end < n and data[end] - data[start] < m:
#         end += 1
#     if end == n:
#         break
#     ans = min(ans, data[end] - data[start])
# print(ans)

# ?????? ?????????
# ???????????? ??????
# N, S = map(int, input().split())
# data = list(map(int, input().split()))
#
# ans = int(1e9)
# start, end = 0, 0
# sum_ = 0
# while True:
#     if sum_ >= S:
#         ans = min(ans, end - start)
#         sum_ -= data[start]
#         start += 1
#     elif end == N:
#         break
#     else:
#         sum_ += data[end]
#         end += 1
#
# print(ans if ans != int(1e9) else 0)

# ????????? + ????????????
# N, S = map(int, input().split())
# data = list(map(int, input().split()))
# prefix_sum = [0] * (N+1)
# for i in range(N):
#     prefix_sum[i + 1] = prefix_sum[i] + data[i]
#
# INF = int(1e9)
# def binary_search(start, end, minus_idx):
#     ret_val = INF
#     while start <= end:
#         mid = (start+end)//2
#         if prefix_sum[mid] - prefix_sum[minus_idx] < S:
#             start = mid + 1
#         else:
#             ret_val = mid
#             end = mid - 1
#     return ret_val
#
# ans = INF
# for start in range(1, N+1):
#     rv = binary_search(start, N, start-1)
#     if rv != INF:
#         ans = min(ans, rv - start + 1)
# print(ans if ans is not INF else 0)

# from itertools import combinations
# data = [int(input()) for _ in range(9)]
# for comb in combinations(data, 7):
#     if sum(comb) == 100:
#         print(*sorted(comb))
#         break


