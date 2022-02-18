# 좌표압축이나 파라메트릭 서치를 제외하면 왠만한건 투포인터 <-> 이진탐색으로 풀이 가능

# 문제1 수 고르기
# 투포인터와 이진탐색 두 가지 방법으로 문제를 해결할 수 있다.
# 아래는 투포인터 방식으로 p2 와 i 는 최대 2n 만큼의 움직임이 있기 떄문에(p2가 끝에 도달하면 끝이다) O(n)만큼의 시간이 소요된다 + 정렬O(nLogn)
# 아래 코드는 리팩토링을 거친 코드니 이해가 잘 안되면 백준- 내 제출메뉴에서 내가 제출한 다른 코드를 확인해보자
# n, m = map(int, input().split())
# data = [int(input()) for i in range(n)]
# data.sort()
#
# rs = int(1e10)
# p2 = 0
# for i in range(n - 1):
#     # p2 = i    ///p2 의 위치는 갱신할 필요가 없음 i 값이 증가하면 정렬ㄹ된 상태기때문에 항상 첫번째 찾은 위치보다 뒤로가게 되어있음 이게 매우 중요하다!!!
#     while p2 < n and data[p2] - data[i] < m:
#         p2 += 1
#     if p2 == n:
#         break
#     rs = min(rs, data[p2] - data[i])
# print(rs)

# 문제2 부분 합
# 이것도 p2의 위치를 굳이 계속 i 위치로 갱신할 필요가 없어
# 그럼 자연스럽게 sum 값도 조정이 필요하지
# 쉽지 않네 여러모로 error 가 발생할 일이 많아
# 두 문제를 풀어봤을 때 투포인터를 사용할 때 두번째 포인터의 이동을 최소화하고
# 잔 계산들도 최대한 최소화 하는게 좋음

# n, s = map(int, input().split())
# data = list(map(int, input().split()))
#
# p2 = 0
# sum = data[0]
# rs = int(1e9)
# for i in range(n):
#     while p2 < n and sum < s:
#         p2 += 1
#         if p2 != n:
#             sum += data[p2]
#     if p2 == n:
#         break
#     rs = min(rs, p2 - i + 1)
#     sum -= data[i]
#
# if rs == int(1e9):
#     print(0)
# else:
#     print(rs)
