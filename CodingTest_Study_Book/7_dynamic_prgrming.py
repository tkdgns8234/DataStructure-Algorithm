# 큰 문제를 작게 나누고, 같은 문제라면 한번씩 풀어 효율적으로 해결하는 알고리즘
# 분할 정복과 유사하나, 중복이 일어나지 않고 작은 문제의 값이 일정함

# 방법 1. memoization 작은 문제들이 반복되고 그 값이 항상 동일할 때 그 값을 저장해두고 사용하는것
# ex 피보나치 수열의 작은 값을 저장해놓고 사용
# 방법 2. top - down
# -> 재귀로 구현하는경우 대부분 top - down 큰 문제가 해결되지 않으면 작은 문제로 이동
# 방법 3. bottom - up
# 작은 문제부터 순차적으로 해결
# 반복문 이용

# 가독성은 top - down 이 더 좋음 (bottom up 에 비해) 이유: 재귀의 점화식을 그대로 쓸 수 있으니 but 작성이 비교적 어려움
# 구미에 맞는걸로 하면 됨
# 참고 사이트: https://galid1.tistory.com/507


# 실전문제2 1로 만들기
# 전 ㅎ ㅕ 감이안온다..
# 해설 보고 다시 풀이
# 이거,, 좀 다르게 출제하면 힘들거같은데, 반복적인 풀이가 필요해보여
# x = int(input())

# cache = [0] * 30001

# for i in range(2, x + 1):
#     cache[i] = cache[i-1] + 1
    
#     if i // 5:
#         cache[i] = min(cache[i//5] + 1, cache[i])
#     if i // 3:
#         cache[i] = min(cache[i//3] + 1, cache[i])
#     if i // 2:
#         cache[i] = min(cache[i//2] + 1, cache[i])

# 실전문제 3 개미 전사
# 이것도 해설 보고도 이해가 잘 안갔어,,
# 코드로 풀이하기가 진짜 쉽지않은데..?
# 풀어보자

# n = int(input())

# array = list(map(int, input().split()))

# #최댓값 출력
# m = [0] * n

# m[0] = array[0]
# m[1] = max(array[0],array[1])

# for i in range(2, n):
#     m[i] = max(m[i-2] + array[i], m[i-1])

# print(m[n-1])

# 실전문제 4 바닥 공사

# n = int(input())

# s = [0] * 1000

# s[0] = 0
# s[1] = 1
# s[2] = 3

# for i in range(3, n+1):
#     s[i] = s[i-1] + s[i-2]*2

# print(s[n] % 796796)

# 실전문제5 효율적인 화폐구성
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

k = [100001] * 101
k[0] = 0

for i in array:
    for j in range(i, m+1):
        if k[j-i] != -1:
            k[j] = min(k[j], k[j-i]+1)

print(k[m])