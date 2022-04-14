# 더 간결하고 좋은 코드가 있다. 플머스 페이지 참고

def fail(index, f):
    sum = 0
    for i in range(index, len(f)):
        sum += f[i][0]
    # 해당 stage 를 클리어한 사람이 없는경우
    if sum == 0:
        return 0
    return f[index][0] / sum
    # 실패율 계산

def solution(N, stages):
    answer = []
    f = [[0, i] for i in range(N + 2)]
    # 실패율, 인덱스 번호

    # 실패율을 위해 계수정렬 형태로 값 대입
    for stage in stages:
        f[stage][0] += 1

    # 실패율 대입
    for i in range(1, N + 1):
        f[i][0] = fail(i, f)

    f.sort(key=lambda x: (-x[0], x[1]))

    for i in range(len(f)):
        idx = f[i][1]
        if idx != 0 and idx <= N:
            answer.append(idx)
    return answer