import math
def is_prime_num(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        a = is_prime_num(i)
        if a % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

# 더 좋은 풀이
# 특정 수의 약수는 대칭 이므로
# 대칭이 아닌 약수는 root 연산을 수행했을때 소수점이 떨어지지 않는 수다
import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer