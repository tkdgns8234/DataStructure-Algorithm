# 수의 최댓값이 10^5 라고 착각했다.
# 아래와 같이 완전탐색형식으로 풀면 무조건 시간초과

# def check(num):
#     temp = list(N)
#     for i in str(num):
#         if i in temp:
#             temp.remove(i)
#         else:
#             return False
#     return True
#
# N = input()
#
# start = 10**(len(N)-1)
# target = 10**len(N)
# numbers = sorted([i for i in range(30, target, 30) if i > start], reverse=True)
#
# ans = -1
# for num in numbers:
#     if check(num):
#         ans = num
#         break
# print(ans)
# # if len(N) < 2: print(-1)

# 다른 풀이를 떠올려보자
# 1. 10만개를 순서를 구별해서 줄세우는것 -> 10만! 로 시간초과
# 2. 그리디적으로 생각해보자...
# 실패

# 완전 수학적인 문제다.
# 3의 배수의 성질을 알아야만 문제를 풀 수 있다.
# 각자리의 합이 3의 배수면 3의 배수이다.
# 현재는 3이 아니라 30의 배수를 확인해야하기떄문에
# 마지막자리에 0 이 포함되어야한다.

# -> 최댓값이 되도록 섞는것이 3의 배수의 최댓값 (자릿수의합이 3의 배수면 3의 배수이므로)
n = sorted(map(int, input()), reverse=True)
if n[-1] != 0:
    print(-1)
elif sum(n) % 3 != 0:
    print(-1)
else:
    print(''.join(map(str, n)))