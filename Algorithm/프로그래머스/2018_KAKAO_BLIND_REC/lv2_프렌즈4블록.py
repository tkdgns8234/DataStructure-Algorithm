import collections


def confirm(arr, m, n):
    bomb_list = set()
    for i in range(m-1):
        for j in range(n-1):
            v = arr[i][j]
            if v != '.' and v == arr[i+1][j] and v == arr[i][j+1] and v == arr[i+1][j+1]:
                bomb_list.add((i, j))
                bomb_list.add((i+1, j))
                bomb_list.add((i, j+1))
                bomb_list.add((i+1, j+1))
    return bomb_list

def move(board, m, n):
    q = collections.deque()
    for j in range(n):
        for i in range(m-1, -1, -1):
            if board[i][j] != '.':
                q.append(board[i][j])
        for i in range(m-1, -1, -1):
            if q:
                board[i][j] = q.popleft()
            else:
                board[i][j] = '.'

def solution(m, n, board):
    board = list(map(list, board))
    answer = 0
    while True:
        bomb_list = confirm(board, m, n)
        if len(bomb_list) == 0:
            break
        else:
            answer += len(bomb_list)
        # bomb
        for x, y in bomb_list:
            board[x][y] = '.'

        move(board, m, n)

    return answer

# v = solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
# print(v)