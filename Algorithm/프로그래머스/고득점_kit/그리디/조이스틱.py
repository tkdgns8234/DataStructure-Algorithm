# 실패
# 이건 이해가 안되는데?
# 나중에 다시보자.. 이해가 안가
# 다른 풀이를 보려고 제출은 했는데 잘 이해가 안간다



def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 최대 이동거리
    move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        move = min([move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += move
    return answer

v = solution('TEST')
print(v)