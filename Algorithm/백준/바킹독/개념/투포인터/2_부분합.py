# 문제2 부분 합
# 이것도 p2의 위치를 굳이 계속 i 위치로 갱신할 필요가 없어
# 그럼 자연스럽게 sum 값도 조정이 필요하지
# 쉽지 않네 여러모로 error 가 발생할 일이 많아
# 두 문제를 풀어봤을 때 투포인터를 사용할 때 두번째 포인터의 이동을 최소화하고
# 잔 계산들도 최대한 최소화 하는게 좋음

n, s = map(int, input().split())
data = list(map(int, input().split()))

p2 = 0
sum = data[0]
rs = int(1e9)
for i in range(n):
    while p2 < n and sum < s:
        p2 += 1
        if p2 != n:
            sum += data[p2]
    if p2 == n:
        break
    rs = min(rs, p2 - i + 1)
    sum -= data[i]

if rs == int(1e9):
    print(0)
else:
    print(rs)
