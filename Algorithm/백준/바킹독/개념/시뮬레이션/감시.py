# # 문제1 감시
# # 못 풀었다
# # 감탄스럽다 아래 주소의 코드
# # #https://developer-ellen.tistory.com/53
# # 좌 우 상 하
# 이거 백트래킹으로 풀었네 백트래킹 + bfs 로 푸니 별거 없어보이긴 하네?
import copy
n, m = map(int, input().split())
cc_info = []
data = []

move_type = [(0, -1), (0, 1), (-1, 0), (1, 0)]
cctv = [
        [],
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 3], [0, 2], [1, 3], [1, 2]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
        [[0, 1, 2, 3]]
        ]

for i in range(n):
    l = list(map(int, input().split()))
    data.append(l)
    for j in range(m):
        if l[j] in [1, 2, 3, 4, 5]:
            cc_info.append((l[j], i, j))


def fill(md, x, y, arr):
    for i in md:
        nx = x
        ny = y
        while True:
            nx = nx + move_type[i][0]
            ny = ny + move_type[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            # 벽인 경우
            if arr[nx][ny] == 6:
                break
            if arr[nx][ny] == 0:
                arr[nx][ny] = 7 # 7 을 cctv가 바라본 지역으로 설정


def dfs(depth, arr):
    global min_val

    if depth == len(cc_info):
        count = 0
        for i in range(len(arr)):
            count += arr[i].count(0)
        min_val = min(min_val, count)
        return
    mode, x, y = cc_info[depth]
    for md in cctv[mode]:
        temp = copy.deepcopy(arr)
        fill(md, x, y, temp)
        dfs(depth + 1, temp)


min_val = int(1e9)
dfs(0, data)
print(min_val)