# 틀렸다
# 끝자리 수를 기준으로 푸는 풀이로는 정답을 도출할 수 없다
# 반례 30, 3021
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     for i in range(3, -1, -1):
#         numbers = sorted(numbers, key=lambda x: x[i if len(x) > i else len(x)-1], reverse=True)
#
#     answer = ''.join(numbers)
#     # 000인 경우를 위해
#     if int(answer) == 0:
#         return '0'
#     else:
#         return answer
# v = solution([30,3021])
# print(v)

# 해설 참고 풀이
# 1. 문자열의 대소비교를 수행하면 자동으로 각 자리수의 ascii 값을 기준으로 정렬하게 된다.
# 2. 0, 0, 0 인 경우 000이 답이 아닌 0 이되도록 처리해야한다
# 3. 반례 30, 3021을 만족하지 못했었는데,
# 각각의 수를 *3 하여 정렬하면 해결된다. <- 문제의 포인트 (최댓값이 1000이기 떄문에 *3)
# 3은 34보다는 뒤에 32보다는 앞에 존재해야 한다는 아이디어 <- 이 아이디어로 위 풀이처럼 풀었는데
# 위 풀이의 경우 예를들어 3, 31 인 경우
# 33, 31 의 대소관계를 비교해서
# 331 이 되도록 했는데
# 두자릿수 이상부터는 문제가 발생할 수 있다.

# 위 코드대로라면
# 30, 3021인 경우
# 3000 3021 로 비교하게 되는데
# 3030 3021 로 비교했어야 했다.

# 정답 코드
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    if numbers.count('0') == len(numbers):
        return '0'
    else:
        return ''.join(numbers)
