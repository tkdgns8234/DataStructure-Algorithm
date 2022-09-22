N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N

for i in range(len(data) - 1, -1, -1):
    consume_days = data[i][0]  # 소요 기간
    if i + consume_days > N:
        continue
    elif i + consume_days == N:
        dp[i] = data[i][1]
    else:
        dp[i] = data[i][1] + max(dp[i+consume_days:])# 현재 상담 금액과 이전 상담 금액의 최댓값의 합
        
#dp 테이블 i를 선택했을때 최댓값

print(max(dp))
