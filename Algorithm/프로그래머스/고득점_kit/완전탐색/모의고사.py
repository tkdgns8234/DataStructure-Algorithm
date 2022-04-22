# index로 특정 패턴을 관리하는 방법
# 이것도 쉬운문제지만, 간단하게 아래처럼 %연산자 사용해 짜는걸 잘 기억해두자

def solution(answers):
    answer = []
    score_list = [0, 0, 0]

    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, ans in enumerate(answers):
        # 1번 수포자
        if ans == i % 5 + 1:
            score_list[0] += 1
        # 2번 수포자
        if ans == pattern2[i % 8]:
            score_list[1] += 1
        # 3번 수포자
        if ans == pattern3[i % 10]:
            score_list[2] += 1

    max_val = max(score_list)
    for i, val in enumerate(score_list):
        if val == max_val:
            answer.append(i+1)

    return answer
