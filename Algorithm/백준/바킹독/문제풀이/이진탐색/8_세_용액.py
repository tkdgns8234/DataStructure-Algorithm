# 8. 세 용액
# 투포인터, 이진탐색 둘 다 가능해보이는데
# 이진탐색: 특정 수를 기준으로 두고 반복 -> 시간초과
# 투포인터로 진행
# 위 문제와 매우 유사해보인다
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
data.sort()

ans1, ans2, ans3 = 1e9, 1e9, 1e9

for i in range(len(data)):
    left, right = i + 1, len(data) - 1
    while left < right:
        sum_ = data[i] + data[left] + data[right]
        if abs(sum_) < abs(ans1 + ans2 + ans3):
            ans1, ans2, ans3 = data[i], data[left], data[right]

        if sum_ == 0:
            break
        elif sum_ < 0:
            left += 1
        elif sum_ > 0:
            right -= 1
print(ans1, ans2, ans3)
