# 처음엔 높이 h 값을 파라메트릭 서치형태로 풀이하는 방법을 떠올렸는데
# h를 변경시킬 기준값이 없기에 불가능했고

# 이 문제는 각 높이마다 부딛히는 장애물의 갯수를 logN 시간안에 찾아야 하는 문제다
# 장애물의 높이를 정렬하고 높이마다 부딛히는 장애물의 갯수를 이진탐색으로 찾을 수 있다.

# 석순과 종유석은 따로 처리를 해야하는데
# 이동하는 높이가 h 일때
# 석순의 경우  석순의 높이가 h 이상이면 부딛히고
# 종유석의 경우 H(동굴의높이) - (h 종유석의 높이) + 1 이 h 이상이면 부딛힌다

# 시복= O(H*log(N))
import bisect
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
s, j = [], []
for i in range(N):
    h = int(input())
    if i % 2 == 0:
        s.append(h)
    else:
        j.append(h)
s.sort()
j.sort()

def check(arr, h): #h 이상의 크기면 부딛힌다, h이상 크기의 갯수를 구하는 이진탐색 함수
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] >= h:
            r = mid - 1
        elif arr[mid] < h:
            l = mid + 1
    return len(arr) - l

# 파이썬은 bisect lib 사용하는게 더 간단!!!!
# def check(arr, h): #h 이상의 크기면 부딛힌다, h이상 크기의 갯수를 구하는 이진탐색 함수
#     return len(arr) - bisect.bisect_left(arr, h)


min_val, count = int(1e9), 0
for i in range(1, H + 1):
    s_count = check(s, i)
    j_count = check(j, H-i+1)

    rs = s_count + j_count
    if rs < min_val:
        min_val = rs
        count = 1
    elif rs == min_val:
        count += 1

print(min_val, count)



# 구간합 풀이는 뭐지? 이진탐색 풀고 떠올려보자
# 처음 구간합 풀이를 떠올렸을 때,
# 입력받은 높이 마다 구간의 합을 구하려고 했다.
# 이렇게되면 완전탐색방식과 동일하게 연산수가 N*M 이 된다.
# 1. 생각을 조금 바꿔서 높이의 갯수를 모두 저장한 후
# 2. h 라는 높이에서 이동하는 경우 경우 높이가 h 이상인 경우 모두 부딛히게 되므로
# 2-1. h일 때 h 이상의 갯수를 모두 더한다
# O(N+H)만에 해결 가능하다
# 구간합으로 풀이를 떠올리기가 쉽진 않은 문제같다.
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
s, j = [0] * (H+1), [0] * (H+1)

for i in range(N):
    h = int(input())
    if i % 2 == 0:
        s[h] += 1
    else:
        j[h] += 1

# 높이 별 부딛히는 장애물 갯수
for i in range(H-1, 0, -1):
    j[i] = j[i] + j[i+1]
    s[i] = s[i] + s[i+1]

min_val = int(1e9)
count = 0
for i in range(1, H+1):
    sum_ = 0
    sum_ += s[i]
    sum_ += j[H-i+1]

    if sum_ < min_val:
        min_val = sum_
        count = 1
    elif min_val == sum_:
        count += 1

print(min_val, count)