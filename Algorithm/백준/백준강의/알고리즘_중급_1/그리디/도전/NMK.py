# 틀린 풀이
# 1부터 N 까지 나열
# 처음 증가수열 N
# 처음 감소수열 1
# 아래 과정을 반복할때마다 증가수열 -1
# 감소수열 +1
# 그다음은 큰 인덱스가 나올때까지 왼쪽으로
# 맨 뒤 요소를 1번째인덱스로 위치하고 나머지 원소 밀기?

# N, M, K = map(int, input().split())
#
# numbers = [i for i in range(1, N+1)]
#
# inc = N
# dec = 1
# now = 1
# for _ in range(1, N):
#     if inc == M and dec == K:
#         print(" ".join(map(str, numbers)))
#         exit(0)
#     num = numbers.pop()
#     numbers.insert(now, num)
#     now += 1
#     inc -= 1
#     dec += 1
# print(-1)

# 풀이를 보면 이해는 되는데
# 너무 지엽적인 문제같은데,,
# pass
