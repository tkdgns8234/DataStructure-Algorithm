# 5. 수 묶기
# 입력으로 들어온 값을 오름차순 정렬
# 값이 1보다 큰 경우 묶는것처럼 계산
# 아래 코드 작성하는데,, 코드가 너무 복잡해졌다
# 가독성 + 간단히 짜는 연습 계속 하자
# 다시풀자
# 매번 문제 해결 방법을 정확히 정의하고 풀어야하는것인가?
# 해당 문제는 수 묶기 규칙을 모두 찾은 후 코딩하면 더 좋은 구조로 짤 수 있을거같다
# 양수, 음수, 0인경우 모두 확인해서
# 묶는 방법을 정의하고 개선 해 나가는방법

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
result = 0
i = len(data)-1
while i >= 0:
    if i == 0:        # 홀수인 경우 and 한 개 남은 경우
        result += data[i]
        break
    else:
        if data[i-1] > 1: # 왼쪽에 있는 값이 1보다 큰 경우 곱셈
            result += data[i]*data[i-1]
            i -= 2
        else:
            if data[i] == 0:
                if i % 2 == 0 and i >= 1 and data[i-1] == 0: # 홀수 개가 남았고 0이 더있으면
                    i -= 1
                    continue
                else:
                    result += data[i]*data[i-1]
                    i -= 2
            else: # -인경우
                result += data[i]

print(result)

# 묶는 방법을 처음에 정확하게 정해놓지 않으면
# 시행착오를 계속 겪게되고 코드도 복잡해진다
# 묶는 방법 (묶었을 때 최대가 되는 방법)
# 0 -> 음수로 처리 -> 이게 이 문제의 포인트 중 하나다
# 1 -> 무조건 더하는게 좋다
# 양수 -> 높은 값 끼리 곱셈
# 음수 -> 낮은 값 끼리 곱셈

n = int(input())
positive = []
negative = []
one = []
for _ in range(n):
    num = int(input())
    if num == 1:
        one.append(num)
    elif num > 1:
        positive.append(num)
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

result = 0
if len(positive) % 2 == 0: #짝수 갯수인 경우
    for i in range(0, len(positive)-1, 2):
        result += positive[i]*positive[i+1]
else:
    for i in range(0, len(positive)-2, 2):
        result += positive[i]*positive[i+1]
    result += positive[len(positive)-1]

if len(negative) % 2 == 0: #짝수 갯수인 경우
    for i in range(0, len(negative)-1, 2):
        result += negative[i]*negative[i+1]
else:
    for i in range(0, len(negative)-2, 2):
        result += negative[i]*negative[i+1]
    result += negative[len(negative)-1]
result += len(one)
print(result)
