def solution(num):
    answer = 0
    while answer < 500:
        if num == 1:
            return answer
        elif num % 2 == 0:
            num /= 2
        elif num % 2 != 0:
            num = num * 3 + 1
        answer += 1
    return -1