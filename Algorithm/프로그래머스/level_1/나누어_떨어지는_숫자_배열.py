def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    return [-1] if not answer else answer
