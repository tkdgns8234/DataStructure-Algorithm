def solution(a, b):
    if a > b: a, b = b, a
    answer = 0
    diff = b - a + 1

    if diff == 1:
        answer = a # a와 b 동일
    elif diff % 2 == 0:
        answer = (a+b) * (diff//2)
    else:
        answer += (a+b)//2
        answer += (a+b) * (diff//2)
    return answer

print(solution(5,3))


# 근본 원리는 같다 구간의 합을 구할 때 3456 이면 45의 합 + 36의 합 이 반복되는 특징을 이용한다
# 아래는 O(n) 의 풀이법인데, a 와 b의 차이가 매우 크므로 O(1)의 풀이방법인 내가 푼 방법이 났다.
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))
