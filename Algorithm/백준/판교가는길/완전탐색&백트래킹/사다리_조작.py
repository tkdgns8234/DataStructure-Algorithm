# 모든 경우의 수 270
# 270개중 3개를 놓는 경우의 수 -> 10만정도
# 3개이상 or 불가 - 1
import sys
input = sys.stdin.readline

def check():
    for col in range(N):
        position = col
        for row in range(H):
            if data[row][position]:
                position += 1
            elif position > 0 and data[row][position-1]:
                position -= 1
        if position != col:
            return False
    return True

def btk(depth, x, y):
    global ans
    if ans <= depth:
        return
    if check():
        ans = min(ans, depth)
    if depth == 3:
        return

    for row in range(x, H):
        if row == x: #라인이 그대로면 y축 계속탐색
            temp = y
        else:
            temp = 0# 라인이 바뀌면 0부터 다시 탐색

        for col in range(temp, N-1):
            if data[row][col] != 1:
                if 0 < col and data[row][col-1] == 1:
                    continue
                if data[row][col+1] == 1:
                    continue
                data[row][col] = 1
                btk(depth+1, row, col + 2)
                data[row][col] = 0

N, M, H = map(int, input().split())
data = [[0]*N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    data[a-1][b-1] = 1

ans = 4
btk(0, 0, 0)
print(ans if ans != 4 else -1)
