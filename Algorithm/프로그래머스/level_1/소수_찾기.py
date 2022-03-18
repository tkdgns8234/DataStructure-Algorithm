import math
# 에라토스테네스의 체
def solution(n):
    answer = 0
    is_prime = [True for _ in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*2, n + 1, i):
                is_prime[j] = False
    return is_prime.count(True) - 2 # 0과 1 제외