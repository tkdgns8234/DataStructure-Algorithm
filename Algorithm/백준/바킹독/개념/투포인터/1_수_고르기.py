# 문제1 수 고르기
# 투포인터와 이진탐색 두 가지 방법으로 문제를 해결할 수 있다.
# 아래는 투포인터 방식으로 p2 와 i 는 최대 2n 만큼의 움직임이 있기 떄문에
# O(n)만큼의 시간이 소요된다 + 정렬O(nLogn)
# 아래 코드는 리팩토링을 거친 코드니 이해가 잘 안되면
# 백준- 내 제출메뉴에서 내가 제출한 다른 코드를 확인해보자
n, m = map(int, input().split())
data = [int(input()) for i in range(n)]
data.sort()

rs = int(1e10)
p2 = 0
for i in range(n - 1):
    # p2 = i    ///p2 의 위치는 갱신할 필요가 없음!!!!
    # i의 증가로 차이가 감소했기 떄문에 p2위치 이후만 탐색
    while p2 < n and data[p2] - data[i] < m:
        p2 += 1
    if p2 == n:
        break
    rs = min(rs, data[p2] - data[i])
print(rs)