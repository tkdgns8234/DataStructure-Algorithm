import math
from itertools import combinations
def is_prime_number(num):
    if num < 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    l = combinations(nums, 3)
    for i in l:
        if is_prime_number(sum(i)):
            answer += 1
    return answer

print(solution([1,2,3,4]))