# 2배 길이의 배열 만들고 원형처리 -> 시계반대방향도 처리 가능
# 가장 긴 것부터 취약지점을 시작으로 차례대로 확인 weak 지점 확인 가능한지

# 아래 풀이가 틀린 이유는
# 그리디 형태로
# 길이가 긴 dist 부터 처리하면 무조건 정답이다 라는 명제가 틀렸다.
# 반례는 아래와 같다
# a = solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30])
# permu로 모든 경우의 수를 구해서 진행해야한다.
# 그리디 형태로 풀이할때 조심하자.. 함부로 그리디라 판단하면 안된다
# 반례를 잘 살펴보고 증명해야한다


def solution(n, weak, dist):
    # weak 의 길이를 2배로 늘린다. (원형을 선형으로 처리)
    weak = weak + [n+i for i in weak]
    # 가장 길게 돌 수 있는 사람부터 확인
    dist.sort(reverse=True)

    answer = int(1e9)
    for start in range(len(weak)//2):
        weak_count = 0 # 포함시킨 취약지점의 갯수
        for idx, d in enumerate(dist):
            point = weak[start] + d

            while start < len(weak):
                if weak[start] <= point:
                    weak_count += 1
                    start += 1
                else:
                    break

            if weak_count >= len(weak)//2:
                answer = min(answer, idx+1)
                print(answer)
                break

    return answer if answer != int(1e9) else -1


# 정답 코드
# weak 포인트 기준이 아니라 투입한 친구 수를 기준으로 진행하네,,
# 특이하다

import itertools
def solution(n, weak, dist):
    length = len(weak)
    # 1. weak 배열의 길이를 2배로 늘리기
    for i in range(length):
        weak.append(weak[i]+n)
    # 2. 투입할 친구의 최솟값을 찾기 위해 최댓값보다 1 큰 값으로 초기화
    answer = len(dist)+1
    # 3. 0부터 length-1까지 start 이동하면서 찾기
    for start in range(length):
        for friends in list(itertools.permutations(dist, len(dist))):
            count = 1 # 투입할 친구 수
            # 현재 친구가 점검 가능한 위치 구하기
            position = weak[start]+friends[count-1]
            # 시작점 부터 모든 취약지점 확인
            for i in range(start, start+length):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i]+friends[count-1]

            answer = min(count, answer)

    if answer > len(dist):
        return -1
    return answer

a = solution(12, [0,10], [1,2])
print(a)