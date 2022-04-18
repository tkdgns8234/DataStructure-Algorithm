# O(n^3 풀이야,,)
# O(n) 으로도 풀 수 있다

# import math
#
# def solution(progresses, speeds):
#     answer = []
#     for i in range(len(progresses)):
#         if progresses[i] >= 100: continue
#         remain = 100 - progresses[i]
#         days = math.ceil(remain/speeds[i])
#
#         count = 1
#         progresses = [progresses[i] + speeds[i]*days for i in range(len(progresses))]
#
#         for idx in range(i+1, len(progresses)):
#             if progresses[idx] >= 100:
#                 count += 1
#             else:
#                 break
#         answer.append(count)
#     return answer
#
# v = solution([93, 30, 55],	[1, 30, 5])
# print(v)

# 개선
# 컨셉: 필요한 days 를 개선해나간다
# import math
#
# def solution(progresses, speeds):
#     answer = []
#     days = math.ceil((100-progresses[0])/speeds[0])
#     count = 1
#     for i in range(1, len(progresses)):
#         if progresses[i] + speeds[i]*days < 100:
#             answer.append(count)
#             days = math.ceil((100 - progresses[i]) / speeds[i])
#             count = 1
#         else:
#             count += 1
#     answer.append(count)
#     return answer
#
# v = solution([93, 30, 55],	[1, 30, 5])
# print(v)

# 더 좋은 코드
# q 활용
# 정석적인 풀이
import math

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        left = math.ceil((100-p)//s)
        if len(Q)==0 or Q[-1][0] < left:
            Q.append([left, 1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

v = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
print(v)



# 더 좋은 코드
# 남은 days 활용
# from math import ceil
#
# def solution(progresses, speeds):
#     daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
#     count = 1
#     retList = []
#
#     for i in range(len(daysLeft)):
#         try:
#             if daysLeft[i] < daysLeft[i + 1]:
#                 retList.append(count)
#                 count = 1
#             else:
#                 daysLeft[i + 1] = daysLeft[i]
#                 count += 1
#         except IndexError:
#             retList.append(count)
#
#     return retList
