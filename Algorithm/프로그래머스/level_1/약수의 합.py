import math

def solution(n):
    answer = 0
    for i in range(1, int(math.sqrt(n))+1):
        if i == math.sqrt(n):
            answer += i
        elif n % i == 0:
            answer += i
            answer += n//i
    return answer

print(solution(5))

#시복은 떨어지지만 간단한 코드
def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])

