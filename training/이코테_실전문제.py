# greedy 알고리즘
# 실전문제 2. 큰 수의 법칙

# n, m, k = map(int, input().split())

# l = list(map(int, input().split()))

# l.sort()

# first = l[n-1]
# second = l[n-2]

# sum = 0
# while True:
#     for i in range(k):
#         if m == 0:
#             break;
#         sum += first
#         m -= 1
#     if m != 0:
#         sum += second
#         m -= 1

# print(sum)

# 실전문제 3 숫자 카드 게임

# n, m = map(int, input().split())

# l = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     row.sort()
#     l.append(row)

# result = 0
# for i in range(n):
#     result = max(result, l[i][0])

# print(result)

# 실전문제4 1이 될 때까지
# 10억 미만인 경우
# n, k = map(int, input().split())

# count = 0
# while n > 1:
#     if n % k == 0:
#         n = n // k
#         count+=1
#     else:
#         n -= 1
#         count+=1
# print(count)

# 10억 이상인 경우
# n, k = map(int, input().split())

# count = 0
# while n > 1:
#     print(n)
#     if n % k != 0:
#         a = n % k
#         if n < k:
#             a -= 1
#         n -= a
#         count += a
#     else:
#         n = n // k
#         count += 1

# print(count)

# 구현 알고리즘

# 왕실의 나이트
# 아래는 좋지못한 풀이
# 이건 그냥 -2-1, -1,-2 형식으로 이동 가능한 좌표 배열을 다 만들어놓고 이동하면 매우 간단해짐

# start = input()

# x = int(start[1])
# y = ord(start[0]) - (ord('a') - 1)

# move = ['L','R','U','D']
# move_x = [0,0,-1,1]
# move_y = [-1,1,0,0]

# pattern = ['LLU','LLD','RRU','RRD','UUL','UUR','DDL','DDR']

# rcount = 0
# count = 0
# for i in pattern:
#     rx,ry = x,y 
#     for k in i:
#         idx = move.index(k)
#         nx = rx + move_x[idx]
#         ny = ry + move_y[idx]
    
#         if nx >= 1 and ny >= 1 and nx < 9 and ny < 9:
#             rx = nx
#             ry = ny
#             count+=1
#         else:
#             break;
#         if count == 3:
#             count = 0
#             rcount += 1

# print(rcount)

# 실전문제3 게임 개발
# pass

#dfs bfs
