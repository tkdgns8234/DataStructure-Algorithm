# 실패
# O(n^2) 풀이로 많은사람들이 통과한듯 보이나
# 실제 10만개의 TC가 추가된다면 통과하지 못할것이다
# 사실상 O(nlogn)이나 O(n)까지 줄이는것은 불가하다
# 문제의 요점은 O(n^2)에서 얼마나 많이 효율적으로 줄여가는지를 보려는거같다
# 아래 코드는 stack을 활용한 코드,
# 나중에 다시 보자 아이디어를 떠올리기 쉽지 않은 코드다


# 참고코드 1
# https://velog.io/@soo5717/프로그래머스-주식가격-Python

# prices = [1, 2, 3, 2, 3, 1] return [5, 4, 1, 2, 1, 0]
def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer

solution([1,2,3,2,3])