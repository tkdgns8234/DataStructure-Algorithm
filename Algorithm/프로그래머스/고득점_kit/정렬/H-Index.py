# 답이 꼭 citations 안에 있지만은 않다,, 꼼꼼하지 못했다.
# max 값부터 -1 씩 줄여가며 확인
# 쉬운 문제인데 놓쳤네

# def solution(citations):
#     citations.sort()
#     val = citations[-1]
#     while val >= 0:
#         for i in range(len(citations)-1, -1, -1):
#             if citations[i] >= val:
#                 if len(citations) - i >= val:
#                     return val
#         val -= 1
#     return val
#
# print(solution([4,6,7,7,7,8,8]))


# 신기한 풀이
def solution(citations):
    citations.sort(reverse=True)
    for i in enumerate(citations, start=1):
        print(i)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([4,6,7,7,7,8,8]))