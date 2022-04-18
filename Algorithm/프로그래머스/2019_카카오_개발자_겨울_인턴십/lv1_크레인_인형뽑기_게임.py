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

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])