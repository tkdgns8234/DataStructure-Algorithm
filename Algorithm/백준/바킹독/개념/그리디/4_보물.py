# 문제4 보물
# 큰 설명이 필요없어보인다
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

result = 0
for i in range(n):
    result += a[i] * b[i]
print(result)