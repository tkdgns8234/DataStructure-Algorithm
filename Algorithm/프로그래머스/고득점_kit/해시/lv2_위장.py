# 이전에 해설을 봤던 문제다..
# 문제를 단순화 하고 푸는
# 단순화: 최소 1개의 의상을 입는 모든 경우의 수
# 예제 1 기준
# head gear  //   eye - wear
#   A                 A
#   B                 X
#   X
# 헤드기어에서 A, B 선택하는경우, 아무것도 고르지 않는 경우 (3) * 2 = 6
# -> 둘다 아무것도 고르지 않는 경우를 뺀다 (-1)
# -> 6-1 ==> 5


from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1

    for key in dic:
        answer *= (dic[key]+1)
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))