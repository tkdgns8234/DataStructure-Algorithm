def solution(N, stages):
    answer = {}
    all = len(stages)

    for i in range(1, N+1):
        if all == 0:
            answer[i] = 0
            continue
        cnt = stages.count(i)
        answer[i] = cnt/all
        all -= cnt

    return sorted(answer, key=lambda x: answer[x], reverse=True)

print(solution(4,[4,4,4,4,4]))
