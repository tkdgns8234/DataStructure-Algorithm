import itertools
import math

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    s = set()
    for i in range(1, len(numbers) + 1):
        for permu in itertools.permutations(numbers, i):
            n = int(''.join(permu))
            s.add(n)
    for i in s:
        if is_prime_number(i):
            answer += 1
    return answer

print(solution('011'))