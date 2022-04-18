# 효율성 테스트 아이디어를 모르겠다.
# 아래 좋은 풀이가 있다.
# 다시 풀어보자.. 정확성 효율성 풀이 다 고려해서

# import bisect
#
# def solution(info, query):
#     new_info, new_queries = [], []
#     for i in info:
#         new_info.append(i.split(' '))
#     for q in query:
#         l = list(q.split(" and "))
#         temp = l[-1]
#         l.pop()
#         l += temp.split(" ")
#         new_queries.append(l)
#
#
#     for i, query in enumerate(new_queries):
#         for q in query:
#             if q == '-':
#                 continue
#             start = bisect.bisect_left(new_info, q)
#             end = bisect.bisect_right(new_info, q)
#
#     answer = []
#     return answer
#
# solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
#          ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])



# 아래 풀이가 어떻게 나왔는가
# 1. 일단 카카오 코테 보면 용량제한은 대부분 없는거같아
# 효율성 테스트도 정해진 시간이 있는건 아니다
# 처음 문제를 접했을 때, prefix sum 과 유사한 방법은 없을까 를 떠올리기도 했는데
# 그 방법과 유사하게 푸는게 맞았다
# info 에 대해 ('-'를 하나씩 대입) 모든 경우의 수를 미리 대입 해 놓는다
# dic[key] = [점수, ..]  // key는 info에서 점수를 제거한 나머지 데이터

# 복습하면서
# dictionary 활용
# defaultdict 활용 해보자


# 좋은 풀이
#https://velog.io/@dogcu/프로그래머스-순위-검색
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score)
    for value in dic.values():
        value.sort()

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
