# 2. 수들의 합2
n, m = map(int, input().split())
data = list(map(int, input().split()))

end = 0
sum_ = 0
count = 0
for start in range(n):
    while sum_ < m and end < n:
        sum_ += data[end]
        end += 1
    if sum_ == m:
        count += 1
    sum_ -= data[start]
print(count)