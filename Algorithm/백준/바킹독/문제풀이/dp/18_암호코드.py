# 18. 암호코드
# 다시
# 블로그 https://jyeonnyang2.tistory.com/55
# 자꾸 dp에서 아이디어가 전혀 떠오르지 않는 이유가 뭘까
# 테이블을 명확히 정의한 후
# 예제를 정확히 써내려가면서
# 예제에대한 규칙성을 찾아내는게 dp다 규칙성을 찾는데 집중해봐
# 어떤원리로 어떤 숫자가 추가되는지 원리를 파악하는과정이야

# 어렵다.
# 블로그 참조
# 다시풀기
# dp[n] = n번째 까지의 모든 암호코드 갯수
# 뒤에서부터 1개 기준 -> 251 로 쳤을 때 (25,1) (2,5,1) -> dp[n-1] 에 1 추가된것
# dp[n] = dp[n-1]
# 뒤에서부터 2개를 묶었을 때 10~26 사이인 경우
# dp[n-2] 추가
# 251  -> 51이 10~26 사이라 가정하면 2,51 -> dp[n-2]갯수 더하면 됨
# dp[n] += dp[n-2] if 10 <= (n-2 ,n-1) <= 26

import sys
input = sys.stdin.readline

nums = list(str(input().strip()))
dp = [0 for _ in range(len(nums) + 1)]
dp[0], dp[1] = 1, 1
if nums[0] == '0':
    print(0)
else:
    for i in range(2, len(nums) + 1):
        if int(nums[i - 1]) > 0:
            dp[i] = dp[i - 1]
        to_int = int(nums[i - 2] + nums[i - 1])
        if 10 <= to_int <= 26:
            dp[i] += dp[i - 2]
    print(dp[len(nums)] % 1000000)