# 다시풀자
# 효율성 실패했었다

# 완전탐색
# 이분탐색 둘 다 풀어보자

# # 완전탐색
# def solution(stones, k):
#     answer = 0
#     while True:
#         zero_count = 0
#         for i in range(len(stones)):
#             if stones[i] != 0:
#                 stones[i] -= 1
#                 zero_count = 0
#             else:
#                 zero_count += 1
#             if zero_count == k:
#                 return answer
#         answer += 1
#     return answer


# 이진탐색 중 파라메트릭 서치유형
# 1 ~ 니니즈 친구들이 최대로 건널 수 있는 수
# 이진탐색
def solution(stones, k):
    answer = 0
    start = 1
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2

        zero_point = 0
        flag = True

        for stone in stones:
            if stone - mid < 0: # stone - mid <= 0 인줄 알았는데 아니다 0인경우는 건널 수 있음 직접 시뮬레이션 해보자
                zero_point += 1
            else:
                zero_point = 0
            if zero_point == k:
                flag = False
                break

        if flag:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

v = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3)
print(v)