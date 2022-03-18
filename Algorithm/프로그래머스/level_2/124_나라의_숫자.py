# 3진법으로 표현 후 1, 2, 4 로 치환하자 -> 표현법 다르다

# def solution(n):
#     answer = ''
#     return answer

# 통과
def solution(n):
    answer = ''
    while n:
        if n%3 ==0:
            answer = str(4) + answer
            n = n//3 - 1
        else:
            answer = str(n%3) + answer
            n = n//3
    return answer

solution(6)