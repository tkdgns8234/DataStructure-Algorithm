# 실패
# 1. 이전 전구가 다르면 다음 스위치를 누른다 까지는 떠올렸는데
# 010 반례에 의해 더 풀어나가지 못했다.


# 해결 방법
# 1. 이전 전구가 다르면 다음 스위치를 누른다
# 2. 첫번째 전구를 키는경우와 안키는 경우 두가지로 나눠서 진행
# -> 첫번째 전구는 이전 전구가 없기 때문
import copy

def swap_two(arr, i):
    arr[i-1] = 1 - arr[i-1]
    arr[i] = 1 - arr[i]

def swap(arr, i):
    if i == N-1:
        swap_two(arr, i)
    else:
        for k in range(-1, 2):
            arr[i - k] = 1 - arr[i - k]

N = int(input())
start = list(map(int, input()))
target = list(map(int, input()))
# 첫 번쨰 전구를 키는 경우와 안키는 경우
case_1, case_2 = copy.deepcopy(start), copy.deepcopy(start)
swap_two(case_1, 1)

ans1, ans2 = 1, 0
for i in range(1, N):
    if case_1[i-1] != target[i-1]:
        swap(case_1, i)
        ans1 += 1
    if case_2[i-1] != target[i-1]:
        swap(case_2, i)
        ans2 += 1

# target과 동일해졌는지 확인
flag1, flag2 = True, True
for i in range(N):
    if case_1[i] != target[i]:
        flag1 = False
    if case_2[i] != target[i]:
        flag2 = False

# 최솟값 갱신
ans = int(1e9)
if flag1:
    ans = min(ans1, ans)
if flag2:
    ans = min(ans2, ans)
# 정답 출력
print(ans if ans != int(1e9) else -1)



# 더 좋은 코드
# https://fre2-dom.tistory.com/55