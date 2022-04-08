# 13. 사다리 조작
# 매우 매우 매우 어려웠다
# 사다리를 1개 놓은것, 2개놓은것, 3개놓은것 모두 확인
# 300C1 + 300C2 + 300C3 하면 만족
# 사다리는 true false로 만들자

# 아래 내용보다 좀 더 쉽게 구현한게 있긴 하네
#https://whwl.tistory.com/34

# 블로그 참조 했음

# def check(depth):
#     for i in range(N):
#         now = i
#         for j in range(H):
#             if data[j][now]:
#                 now += 1
#             elif now > 0 and data[j][now -1]:
#                 now -= 1
#         if now != i:
#             return False
#     return True
#
#
# def btk(depth, x, y):
#     global result
#     if result <= depth:
#         return
#     if check(depth):
#         result = min(result, depth)
#     if depth == 3:
#         return
#
#     for i in range(x, H):
#         if i == x: #라인이 그대로면 y축 계속탐색
#             temp = y
#         else:
#             temp = 0# 라인이 바뀌면 0부터 다시 탐색
#         for j in range(temp, N-1):
#             if not data[i][j]:
#                 if j >= N-1 and data[i][j+1]:
#                     continue
#                 if j > 0 and data[i][j-1]:
#                     continue
#                 data[i][j] = True
#                 btk(depth + 1, i, j + 2)
#                 data[i][j] = False
#
# # 세로선, 가로선 갯수, 세로선마다 가로선의 갯수
# N, M, H = map(int, input().split())
# data = [[False] * N for _ in range(H)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     data[a-1][b-1] = True
#
# result = 4
# btk(0, 0, 0)
# print(result if result != 4 else -1)