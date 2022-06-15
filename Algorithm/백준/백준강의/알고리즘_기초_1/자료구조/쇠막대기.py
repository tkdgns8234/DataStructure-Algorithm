# 처음 쇠막대기 갯수 + 레이저 시, 현재 열려있는 괄호의 갯수

# data = input()
# answer = 0
# for i in range(len(data)-1):
#     if data[i] == '(':
#         if not data[i+1] == ')':
#             answer += 1
#
# left_cnt, i = 0, 0
# while i < len(data):
#     if data[i] == '(':
#         if data[i+1] == ')':
#             answer += left_cnt
#             i += 2
#             continue
#         else:
#             left_cnt += 1
#     else:
#         left_cnt -= 1
#     i += 1
#
# print(answer)

# 더 좋은 코드(이전 작성 코드)
data = list(input())
stack = []
cnt = 0
for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        if data[i-1] == '(': # 레이저면
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)