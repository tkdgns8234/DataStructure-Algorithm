def solution(board, moves):
    answer = 0
    result = []
    col_length = len(board)
    for move in moves:
        for l in range(col_length):
            if board[l][move-1] != 0:
                result.append(board[l][move-1])
                board[l][move-1] = 0
                break
        if len(result) >= 2 and result[-1] == result[-2]:
            answer += 2
            result.pop(-1)
            result.pop(-1)

    return answer