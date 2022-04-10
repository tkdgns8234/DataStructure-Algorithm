# 잘 했는데, 투포인터를 좀 더 간결하고 가독성 좋게 변경하자. (완료)
# 백준 제출 확인

import math

def get_prime_number(n):
    is_prime = [True] * (n+1)
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    p = []
    for i in range(2, n+1):
        if is_prime[i]:
            p.append(i)
    return p


N = int(input())
prime_number = get_prime_number(N)
rs = 0
p2 = 0
sum_ = 0
p_len = len(prime_number)

for i in range(p_len):
    while p2 < p_len and sum_ < N:
        sum_ += prime_number[p2]
        p2 += 1
    if sum_ == N:
        rs += 1
    sum_ -= prime_number[i]

print(rs)