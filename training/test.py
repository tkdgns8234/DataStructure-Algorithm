
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
def reculsive(num):
    if num == 1:
        return '*'
    priv = reculsive(num//3)
    arr = []

    for i in range(3):
        for j in range(3):
            if num//3 <= i < num//3*2:
                if num//3 <= j < num//3*2:
                    arr.append(' ')
                    continue
            arr.append(priv)
    return arr

n = int(input()) # 3
print(reculsive(n))
print('\n'.join(reculsive(n)))
# rs = reculsive(n)