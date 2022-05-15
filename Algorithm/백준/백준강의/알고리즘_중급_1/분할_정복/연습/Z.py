# 시작점, 크기를 분할정복
# 시작점 오른쪽, 아래, 오른쪽아래를 차례로 방문
# 매개변수 = 시작점, 크기
# 맞았지만 완전탐색은 시간초과가 발생하네,,
# 위치를 찾는것이 추가되어야함

def dfs(x, y, n):
    global ans

    if n == 1:
        for move_x, move_y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            ans += 1
            if [x+move_x, y+move_y] == [R, C]:
                print(ans)
                exit(0)
        return
    else:
        split = (2**n)//2
        for i in range(2):
            for j in range(2):
                nx = x+i*split
                ny = y+j*split
                if nx <= R < nx + split  and ny <= C < ny + split:
                    dfs(x+i*split, y+j*split, n-1)
                else:
                    ans += (split**2)



N, R, C = map(int, input().split())
ans = -1
dfs(0, 0, N)