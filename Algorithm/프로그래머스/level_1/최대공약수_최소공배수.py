import math
def solution(n, m):
    answer = []
    # 최대공약수
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    # 최소공배수
    for i in range(max(n,m), n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
            
    # lcm은 python 3.9 에서 업데이트 되었으나 사용 안됨
    # answer = []
    # answer.append(math.gcd(n, m))
    # answer.append(math.lcm(n, m))
    return answer
print(solution(3,12))
