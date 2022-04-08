# 12. 경사로
# 실패 다시풀기
# 문제점 1. 코드가 길어졌어
# 원인은? 구현을 어떻게 할지는 정하고 시작했는데
# 1. check 함수에서 매개변수 하나로 row, col 동시에 처리할순없을까 고민을 했었어야했어
# 2. while문보단 for 문을쓰는게 훨씬 깔끔해지고 편해져
# 급하다고 코드를 막 치지 말고 조금만 더 생각하면서 치자..
# 다시풀자

import sys
input = sys.stdin.readline
ROW = 0
COLUM = 1

def check(x, y, direction):
    if direction == ROW:
        build_point = []
        while y < N-1:
            if data[x][y] == data[x][y + 1]:
                y += 1
                continue
            elif data[x][y] - data[x][y + 1] == 1: #높이 차이가1인경우 왼쪽이 더 높음
                if N - y >= L: #경사로 길이만큼 설치 가능 여부 확인
                    temp = y
                    if L == 1:
                        if temp not in build_point:
                            build_point.append(temp)
                        else:
                            return False
                        y+=1
                        continue

                    for _ in range(L-1):
                        if temp in build_point or (temp+1) in build_point:
                            return False
                        if data[x][temp] == data[x][temp + 1]:
                            build_point.append(temp)
                            temp += 1
                        else:
                            return False
                    build_point.append(temp + 1)
                else:
                    return False
            elif data[x][y] - data[x][y + 1] == -1: #높이 차이가-1인경우 오른쪽이 더 높음
                if y >= L-1: #경사로 길이만큼 설치 가능 여부 확인
                    temp = y
                    if L == 1:
                        if temp not in build_point:
                            build_point.append(temp)
                        else:
                            return False
                        y+=1
                        continue

                    for _ in range(L-1):
                        if temp in build_point or (temp-1) in build_point:
                            return False
                        if data[x][temp] == data[x][temp-1]:
                            build_point.append(temp)
                            temp -= 1
                        else:
                            return False
                    build_point.append(temp - 1)
                else:
                    return False
            else:
                return False
            y += 1

    elif direction == COLUM:
        build_point = []
        while x < N-1:
            if data[x][y] == data[x + 1][y]:
                x += 1
                continue
            elif data[x][y] - data[x + 1][y] == 1: #높이 차이가1인경우 왼쪽이 더 높음
                if N - x >= L: #경사로 길이만큼 설치 가능 여부 확인
                    temp = x
                    if L == 1:
                        if temp not in build_point:
                            build_point.append(temp)
                        else:
                            return False
                        x+=1
                        continue

                    for _ in range(L-1):
                        if temp in build_point or (temp+1) in build_point:
                            return False
                        if data[temp][y] == data[temp+1][y]:
                            build_point.append(temp)
                            temp += 1
                        else:
                            return False
                    build_point.append(temp + 1)
                else:
                    return False
            elif data[x][y] - data[x+1][y] == -1: #높이 차이가-1인경우 오른쪽이 더 높음
                if x >= L-1: #경사로 길이만큼 설치 가능 여부 확인
                    temp = x
                    if L == 1:
                        if temp not in build_point:
                            build_point.append(temp)
                        else:
                            return False
                        x+=1
                        continue

                    for _ in range(L-1):
                        if temp in build_point or (temp-1) in build_point:
                            return False
                        if data[temp][y] == data[temp-1][y]:
                            build_point.append(temp)
                            temp -= 1
                        else:
                            return False
                    build_point.append(temp - 1)
                else:
                    return False
            x += 1
    return True


N, L = map(int, input().rstrip().split())
data = [list(map(int, input().rstrip().split())) for _ in range(N)]
result = 0
for i in range(N):
    if check(i, 0, ROW):
        print('row', i)
        result += 1
    if check(0, i, COLUM):
        print('col',i)
        result += 1
print(result)

# 12. 경사로 재풀이
# 완료
# import sys
# input = sys.stdin.readline
#
# def check(arr):
#     build = [False] * N
#     for i in range(N-1):
#         if arr[i] == arr[i+1]:
#             continue
#         elif abs(arr[i] - arr[i + 1]) > 1:
#             return False
#         elif arr[i]-arr[i+1] == 1: # 좌측이 더 큰 경우 오른쪽에 배치
#             for j in range(i+1, i+1+L):
#                 if 0 <= j < N:
#                     if arr[i+1] == arr[j] and not build[j]: # 바닥이 평평한지 확인
#                         build[j] = True
#                     else:
#                         return False
#                 else:
#                     return False
#         elif arr[i]-arr[i+1] == -1: # 우측이 더 큰 경우 좌측에 배치
#             for j in range(i, i-L, -1):
#                 if 0 <= j < N:
#                     if arr[i] == arr[j] and not build[j]: # 바닥이 평평한지 확인
#                         build[j] = True
#                     else:
#                         return False
#                 else:
#                     return False
#     return True
#
# N, L = map(int, input().rstrip().split())
# data = [list(map(int, input().rstrip().split())) for _ in range(N)]
#
# result = 0
# for i in range(N):
#     if check(data[i]): # 행
#         result += 1
#
#     temp = []
#     for j in range(N):
#         temp.append(data[j][i])
#     if check(temp): # 열
#         result += 1
#
# print(result)
