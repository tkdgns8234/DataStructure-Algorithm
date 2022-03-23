# 문제3 로프
# 한번에 맞아버렸다..
# 잘 모르겠을 땐 직접 그림을 그리면서 해결하는게 아주 큰 도움이 된다
# 루프의 크기를 오름차순으로 정렬한 후
# 작은 수 부터 본인의 무게 * (자기보다 큰 수의 갯수) 를 계속 계산한다
# => 최대 중량 계산가능
# 시간복잡도도 충분

n = int(input())
data = [int(input()) for _ in range(n)]

data.sort()
result = []

for i in range(n):
    result.append(data[i] * (n - i))

result.sort()
print(result[n-1])