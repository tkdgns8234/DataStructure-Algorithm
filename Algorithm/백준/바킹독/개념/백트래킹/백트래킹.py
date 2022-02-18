# 문제 N과 M (1)
# n, m = map(int, input().split())
#
# arr = []
#
# def dfs(i):
#     if len(arr) == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(1, n + 1):
#         if i not in arr:
#             arr.append(i)
#             dfs(i)
#             arr.pop()
#
# dfs(0)

# 문제2 N과 m (2)
# n, m = map(int, input().split())
# arr = []
#
# def dfs(start):
#     if len(arr) == m:
#         print(" ".join(map(str, arr)))
#     for i in range(start, n + 1):
#         if i not in arr:
#             arr.append(i)
#             dfs(i + 1)
#             arr.pop()
#
# dfs(1)

# 문제3 n 과 m (3)
# n, m = map(int, input().split())
#
# arr = []
#
# def dfs(i):
#     if len(arr) == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(1, n + 1):
#         arr.append(i)
#         dfs(i + 1)
#         arr.pop()
#
# dfs(0)

# 문제4 n과 m (4)
# n, m = map(int, input().split())
#
# arr = []
#
# def dfs(start):
#     if len(arr) == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(start, n + 1):
#         arr.append(i)
#         dfs(start + 1)
#         arr.pop()
# dfs(start)

# 문제5 n과 m (5)
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
#
# temp = []
#
# def dfs():
#     if len(temp) == m:
#         print(" ".join(map(str, temp)))
#     for i in range(len(arr)):
#         if arr[i] not in temp:
#             temp.append(arr[i])
#             dfs()
#             temp.pop()
# dfs()

# 문제6 n-Queen
# n = int(input())
# cnt = 0
#
# # y축 겹치는지
# issue1 = [False] * 100
# # 우측 위쪽 대각선 겹치는지
# issue2 = [False] * 100
# # 좌측 위쪽 대각선 겹치는지
# issue3 = [False] * 100
#
# def dfs(cur):
#     global cnt
#     if cur == n:
#         cnt += 1
#         return
#     for i in range(n):
#         if issue1[i] or issue2[cur+i] or issue3[cur-i+n-1]:
#             continue
#         issue1[i] = True
#         issue2[cur+i] = True
#         issue3[cur-i+n-1] = True
#         dfs(cur + 1)
#         issue1[i] = False
#         issue2[cur + i] = False
#         issue3[cur - i + n - 1] = False
#
# dfs(0)
# print(cnt)

# 문제7 부분 수열의 합
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
# cnt = 0
# def dfs(depth, sum):
#     if depth == n:
#         return 0
#     # 맨 처음이 0인경우는 없음 숫자를 일단 하나를 넣어야지..
#     # 그래서 더한 경우 m 과 같은지 확인한다
#     if sum + arr[depth] == m:
#         global cnt
#         cnt += 1
#     # 해당 숫자를 포함한 경우와 포함하지 않은 두가지 가지치기
#     dfs(depth + 1, sum + arr[depth])
#     dfs(depth + 1, sum)
#
# dfs(0, 0)
# print(cnt)