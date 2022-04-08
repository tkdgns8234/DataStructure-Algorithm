# Q11 뱀
#방향 전환 상수
LEFT = 'L'
RIGHT = 'D'

# left, right, up, down
side_type = ['U','R','D','L']
move_type = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 보드의 크기
n = int(input())
# 사과의 갯수
k = int(input())

graph = [[0] * (n+1) for i in range(n+1)]

# 0 은 맵
# 1 은 뱀의 몸통
# 사과는 3으로 지정
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 3

# 방향전환 횟수
rotation = []
L = int(input())
for i in range(L):
    l = input().split()
    rotation.append((int(l[0]), l[1]))

def rotation_left_right(type, side):
    result = 0
    now = side_type.index(side)
    if type == RIGHT:
        if now < 3:
            result = now + 1
        else:
            result = 0
    else:
        if now == 0:
            result = 3
        else:
            result = now - 1
    return side_type[result]

x = y = 1
graph[x][y] = 1
time = 0
side = side_type[1]

tail_position = 0
remember_move = []
remember_move.append((x, y))

while True:
    for i in rotation:
        if i[0] == time:
            side = rotation_left_right(i[1], side)

    for i in range(len(side_type)):
        if side == side_type[i]:
            nx = x + move_type[i][0]
            ny = y + move_type[i][1]

    if nx < 1 or ny < 1 or nx >= len(graph) or ny >= len(graph):
        time += 1
        break
    if graph[nx][ny] == 1:
        time += 1
        break
    # 사과가 아닌 경우
    if graph[nx][ny] != 3:
        # 꼬리 자르기
        tail_x, tail_y = remember_move[tail_position]
        graph[tail_x][tail_y] = 0
        # 꼬리 이동
        tail_position += 1

    graph[nx][ny] = 1
    x, y = nx, ny
    remember_move.append((x, y))
    time += 1

print(time)
