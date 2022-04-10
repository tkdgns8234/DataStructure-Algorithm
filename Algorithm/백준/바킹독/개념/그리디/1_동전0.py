# 문제1 동전0
# 한방에 성공! 각 동전이 배수 형태로 존재하기 때문에 그리디로 해결 가능
# dp 로 해결하려는경우 O(nk)로 10억이 훨씬넘어가서 풀 수 없다
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
while True:
    if k == 0:
        break
    for c in coins[::-1]:
        if k // c > 0:
            count += k // c
            k = k % c
            break

print(count)