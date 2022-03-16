# 진수 표현 방식을 참고한 후에 다시 풀었다 아래 2진수 표현방법을 참고하자
# 몫을 나눈 나머지를 기록하는 방식
def get_3rd_num(n, l):
    a, b = divmod(n, 3)
    l.append(b)
    if a == 0:
        return list(reversed(l))
    else:
        return get_3rd_num(a, l)

def solution(n):
    answer = 0
    l = []
    l = get_3rd_num(n, l)
    for i in range(len(l)):
        answer += (3**i)*l[i]
    return answer

print(solution(5))

# 2진법 구하기
# 재귀 호출을 이용한 풀이
# 2로 나눈 나머지를 계속 기록하는 방식
# divmod 함수 이용

# def getBinaryNum(n, lists):
#     a, b = divmod(n, 2)
#     lists.append(b)
#     if a == 0 :
#         return lists
#     else:
#         return getBinaryNum(a, lists)
#
# answerList = []
# answer = list(reversed(getBinaryNum(5,answerList)))
#
# print("".join(map(str, answer)))

# 좀 더 나은 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer