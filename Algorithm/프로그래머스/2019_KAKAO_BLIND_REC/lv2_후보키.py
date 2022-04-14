# 한 열씩 중복이 발생하는지 확인
# 중복 없으면 후보키
# 중복 있는것만 구성해서 남은 갯수만큼 반복
# 반복 후 새로추가된 후보키 없으면 종료
# 실패
# 원인: 일단 로직을 너무 복잡하게 생각했다.
# 단순 명료하게 짜는게 좋아보이네 너무 효율성만 따지지 말고 적절히

# low가 8이기때문에 모든 후보키 조합을 구해놓고 연산해도 괜찮다.
# 로직
# 1. 모든 조합 구하기
# 2. 유일성 만족하는 경우 + 1
# 3. 최소성 만족하지 않으면 제거

# from itertools import combinations
#
# def confirm():
#     pass
#
# def solution(relation):
#     answer = 0
#
#     row = len(relation)
#     col = len(relation[0])
#
#     # 하나의 colum이 후보키 인 경우
#     keys = [i for i in range(col)]
#     for i in keys:
#         same = False
#         for j in range(row-1):
#             if relation[j][i] == relation[j+1][i]:
#                 same = True
#         if not same:
#             answer += 1
#             keys.remove(i)
#
#     # 후보키의 모든 조합 확인
#     same = True
#     while keys or same:
#         same = False
#         num = 2
#         for comb in combinations(keys, num):
#             temp_keys = []
#             for i in range(row):
#                 k = ''
#                 for c in comb:
#                     k += relation[row][c]
#                 temp_keys.append(k)
#     return answer


# 나중에 다시 풀자
# 집합을 이용한 아주 좋은 풀이
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    # 유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:  # 유일성
            put = True

            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break

            if put: unique.append(i)

    return len(unique)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

# test = [(1,2,),(1,),(1,),(1,2,3,4)]
# set_ = [(1,2,3,4)]
# if set(set_).issubset(set(test)):
#     print('yes')