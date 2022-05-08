# N, M, K = map(int, input().split())
#
# while K:
#     K -= 1
#     if N == 0:
#         M -= 1
#         continue
#     elif M == 0:
#         N -= 1
#         continue
#
#     if N//M >= 2:
#         N -= 1
#     else:
#         M -= 1
# ans = min(M, N//2 if N > 1 else 0)
# print(ans)


# 더 좋은 풀이
n, m, k = map(int, input().split())	# n 여학생 수, m 남학생 수, k 인턴쉽 학생 수
result = 0

while n >= 2 and m >= 1 and n + m >= k + 3:	# 2명 , 1명 팀 만들 수 있고, 인턴쉽도 보낼 수 있는 수 일때
    n -= 2	# 빼주고
    m -= 1	# 빼주고
    result += 1	# 팀 수는 하나씩 더해준다
print(result)