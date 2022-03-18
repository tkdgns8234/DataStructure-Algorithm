def solution(n):
    answer = '수박' * (n // 2)
    if n % 2 != 0:
        answer += '수'
    return answer

# 더 좋은 풀이
# 대박;
def water_melon(n):
    s = "수박" * n
    return s[:n]