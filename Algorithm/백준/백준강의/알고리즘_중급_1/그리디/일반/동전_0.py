# 각 동전이 배수형태이기때문에 greedy 사용 가능
K, target = map(int, input().split())
coins = list(reversed([int(input()) for _ in range(K)]))

total = 0
cnt = 0
while total != target:
    cnt += 1
    for coin in coins:
        if total + coin <= target:
            total += coin
            break
print(cnt)

# 더 좋은 방법(이전에 풀었던 코드)
# 가능한 coin 만큼 나눗셈 수행
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

