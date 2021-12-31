##문제 1 상하좌우
# n 은 공간의 크기
# n = int(input())
# plan = list(input().split())

# x = 1
# y = 1

# for word in plan:
#     if word == 'L':
#         if y > 1:
#             y -= 1
#     elif word == 'R':
#         if y < n:
#             y += 1
#     elif word == 'U':
#         if x > 1:
#             x -= 1
#     elif word == 'D':
#         if x < n:
#             x += 1

# print(x, y)
# 맞는데 더 좋은 방법이 있다
# n = int(input())
# plans = input().split()

# move_types = ['L', 'R', 'U', 'D']
# move_x = [0,0,-1,1]
# move_y = [-1,1,0,0]

# x,y = 1,1 
# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표구하기
#     for move_type in move_types:
#         if plan == move_type:
#             temp_x, temp_y = x + move_x[move_type], y + move_y[move_type]
#     # 범위를 넘어가는경우 무시
#     if temp_x < 1 or temp_x > n or temp_y < 1 or temp_y > n:
#         continue
#     x, y = temp_x, temp_y

# print(x,y)


## 연습문제 시각
# n = int(input())
# 실패...
# 수학적 규칙을 찾기 어려운경우 빨리 다른방법을 생각하자

# 풀이 보고 다시 시도
# n = int(input())

# count = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             res = str(i) + str(j) + str(k)
#             if '3' in res:
#                 count += 1
# print(count)


## 문제 2 실전문제 왕실의 나이트
# 다시 풀이
# x_list = [None,a,b,c,d,e,f,g,h]

# s = str(input())
# x,y = x_list.index(s[0]), int(s[1])

# minimum = 1
# maximum = 8

# 다시풀자
# val = input()

# # x 좌표의 경우 a ~ h 를 숫자로 변환
# x = ord(val[0]) - (ord('a') + 1)
# y = int(val[1])

# moves = [(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(1,-2),(-1,-2)]
# x,y = 1,1

# count = 0
# for move in moves:
#     nx, ny = x + move[0], y + move[1]
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     count+=1
    
# print(count)

## 문제 3 게임 개발
#시간 초과됨.. 일단 굳이 move 랑 sides 배열 따로쓰지말고 좌로 회전시킬 때 반대 방향으로 돌게 변경하면됨
#나머진 잘 했음 변수이름 좀 더 적절하게 바꾸고

def rotate(move):
    if move == 3:
        return 0
    else:
        return move+1

# 세로 n 가로 m
move = ['U','L','D','R']
move_x = [-1,0,1,0]
move_y = [0,-1,0,1]

n, m = map(int, input().split())
x, y, cur_side = map(int, input().split())
sides = ['U','R','D','L']
cur_side = move.index(sides[cur_side])

cmap = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    cmap[i] = list(map(int, input().split()))

count = 1
side_maximum_count = 0

while True:
    nx, ny = 0, 0    
    cur_side = rotate(cur_side)
    nx, ny = x + move_x[cur_side], y + move_y[cur_side]
    if nx < 0 or ny < 0 or nx > n or ny > m:
        continue
    
    if cmap[nx][ny] == 0:
        cmap[x][y] = 1
        x, y = nx, ny
        count += 1
        side_maximum_count = 0
        continue
    else:
        side_maximum_count += 1
    if side_maximum_count == 4:
        nx, ny = x - move_x[cur_side], y - move_y[cur_side]
        if cmap[nx][ny] == 1:
            break;
        side_maximum_count = 0


print(count)

# 입력
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 출력: 2