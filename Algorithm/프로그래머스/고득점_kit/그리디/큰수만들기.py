# 풀이과정
# 1. 정렬해서 작은 수 부터 제거하는 방법 -> 실패
# 2. i 번째 수보다 뒤에 더 큰 수가 있다면 제거하는 방법 -> 실패
# 3. 인터넷 풀이 참고
# 2번 풀이처럼 뒤에 모든 수를 참고하는게 아니라
# 3.1 들어가려는 숫자보다 앞에 더 큰 숫자가 있는지만 고려, stack 구조로 작성
# 스택을 활용한 구현 방법을 잘 익혀놔야겠다.
# 구현 컨셉만 잘 잡으면 구현은 그냥 하면 돼.
# 컨셉을 잘 잡아야한다

# def solution(number, k):
#     stack = []
#
#     number = list(map(int, number))
#     for i in number:
#         if len(stack) == 0 or stack[-1] > i:
#             stack.append(i)
#         else:
#             while stack and stack[-1] < i and k > 0:
#                 stack.pop()
#                 k -= 1
#             stack.append(i)
#     while k:
#         stack.pop()
#         k -= 1
#     return ''.join(map(str, stack))

# v = solution("654321", 5)
# print(v)


# 수정
def solution(number, k):
    stack = []

    number = list(map(int, number))
    for i in number:
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    stack = stack[:len(stack)-k]
    return ''.join(map(str, stack))


v = solution("1924", 2)
print(v)
