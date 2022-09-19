from collections import deque

APPLE = 1

def rotate(side):
    global currentRotate
    if side == "L":
        currentRotate -= 1
    else:
        currentRotate += 1

    if currentRotate == -1:
        currentRotate = 3
    if currentRotate == 4:
        currentRotate = 0


N = int(input())
K = int(input())
applePos = []
for i in range(K):
    x, y = map(int, input().split())
    applePos.append((x-1, y-1))

L = int(input())
rotateInfo = []
for i in range(L):
    a, b = input().split()
    rotateInfo.append((int(a), b))

data = [[0] * N for _ in range(N)]
for x, y in applePos:
    data[x][y] = APPLE

direct = [0, 1, 2, 3]  # 북, 동, 남, 서
move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

currentRotate = 1  # 동쪽을 바라본다.
tail = deque()
tail.append([0, 0])
time = 0
x, y = 0, 0
while True:
    nx = x + move_x[currentRotate]
    ny = y + move_y[currentRotate]
    time += 1

    if 0 <= nx < N and 0 <= ny < N:
        if [nx, ny] in tail:
            print(time)
            break
        else:
            x = nx
            y = ny
            tail.append([x, y])
            if data[x][y] != APPLE:
                if len(tail) != 0:
                    tail.popleft()
            data[x][y] = 0
            if len(rotateInfo) != 0 and time == rotateInfo[0][0]:
                rotate(rotateInfo.pop(0)[1])
    else:
        print(time)
        break
