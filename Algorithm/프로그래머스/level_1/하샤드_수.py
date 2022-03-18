def solution(x):
    return True if x / sum(map(int, str(x))) == int(x / sum(map(int, str(x)))) else False

# 더 좋은 코드
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))