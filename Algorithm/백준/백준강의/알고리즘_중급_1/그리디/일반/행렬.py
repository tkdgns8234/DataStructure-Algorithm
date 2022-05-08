N, M = map(int, input().split())
board1, board2 = [], []
for _ in range(N):
    board1.append(list(map(int, input())))
for _ in range(N):
    board2.append(list(map(int, input())))

def solve(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board1[i][j] == 0:
                board1[i][j] = 1
            else:
                board1[i][j] = 0

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if board1[i][j] != board2[i][j]:
            solve(i, j)
            ans += 1

for i in range(N):
    for j in range(M):
        if board1[i][j] != board2[i][j]:
            print(-1)
            exit()
print(ans)