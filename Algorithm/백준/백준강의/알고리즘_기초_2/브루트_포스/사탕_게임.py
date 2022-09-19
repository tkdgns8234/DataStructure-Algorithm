
# 두 위치 바꾸고
# 두 위치부터 상하좌우 확인

from collections import deque

reverse_move_type = [(1, 0), (-1, 0), (0, -1), (0, 1)]
move_type = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def search(x, y, move):
    q = deque()
    q.append((x, y))

    cnt = 1
    while q:
        x, y = q.popleft()
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < N and 0 <= ny < N:
            if data[x][y] == data[nx][ny]:
                q.append((nx, ny))
                cnt += 1
    return cnt


N = int(input())
data = [list(input()) for _ in range(N)]
answer = 0

for x in range(N):
    for y in range(N):
        for move in move_type:
            answer = max(answer, search(x, y, move))
            if answer == N:
                print(answer)
                exit()

for x in range(N):
    for y in range(N):
        # 4방향 변경
        for move in move_type:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < N:
                data[x][y], data[nx][ny] = data[nx][ny], data[x][y]
                # 변경 후 변경된 위치의 4방향 확인
                for move_idx in range(4):
                    answer = max(answer, search(x, y, move_type[move_idx]) + search(x, y, reverse_move_type[move_idx]) - 1)
                    answer = max(answer, search(nx, ny, move_type[move_idx]) + search(nx, ny, reverse_move_type[move_idx]) - 1)
                data[x][y], data[nx][ny] = data[nx][ny], data[x][y]

print(answer)




# 좀 더 효율적인 방법
# 아래 코드에서 주의깊게 봐야할 점 check() 함수를 통해
# 행과 열을 검사하는 방법
# 상하좌우 모두 확인하는게 아니라 상, 좌 위치는 이미 확인했기떄문에 확인하지 않는 방법

import sys

input = sys.stdin.readline


def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer


n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j + 1 < n:
            # 인점한 것과 바꾸기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp = check(arr)

            if temp > answer:
                answer = temp

            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        # 행 바꾸기
        if i + 1 < n:
            # 인점한 것과 바꾸기
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp = check(arr)

            if temp > answer:
                answer = temp

            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(answer)