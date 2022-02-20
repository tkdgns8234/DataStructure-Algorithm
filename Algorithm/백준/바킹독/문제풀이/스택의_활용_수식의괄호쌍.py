# 1. 좋은 단어
# n = int(input())
# count = 0
# for _ in range(n):
#     words = list(input())
#     stack = []
#     for i in range(len(words)):
#         if stack and words[i] == stack[-1]:
#             stack.pop()
#         else:
#             stack.append(words[i])
#     if len(stack) == 0:
#         count += 1
# print(count)

# 2. 쇠막대기
# 괄호 안에 있는 레이저갯수 + 1 개만큼으로 나뉨
# 이걸 못푸네 ㅋㅋㅋㅋㅋ
# 다시풀자
# data = list(input())
# laser_cnt = [0] * 100000
# stack = []
#
# rs = 0
# for i in range(len(data)):
#     if data[i] == '(':
#         stack.append((i, '('))
#     else:
#         if stack[-1][1] == '(':
#             for j in stack:
#                 laser_cnt[j[0]] += 1
#             stack.append((i, ')'))
#         else:
#             while True:
#                 stack.pop()
#                 stack.pop()
#                 if stack[-1][1] == '(':
#                     rs += laser_cnt[stack[-1][0]]
#                     stack.pop()
#                     break
# print(rs)

# 쇠막대기 재풀이
# 블로그 참조 후 다시풀음..
# 이걸 못풀다니,, 자괴감이 드네 간단한 코드지만 이 방법을 떠올리기가 쉽지 않았다
# 좀 더 침착하게 풀자
# data = list(input())
# stack = []
# cnt = 0
# for i in range(len(data)):
#     if data[i] == '(':
#         stack.append('(')
#     else:
#         if data[i-1] == '(': # 레이저면
#             stack.pop()
#             cnt += len(stack)
#         else:
#             stack.pop()
#             cnt += 1
# print(cnt)

# 괄호의 값
# 코드가 너무 길긴하네
# data = list(input())
# stack = []
# for i in data:
#     if i == '(' or i == '[':
#         stack.append(i)
#     else:
#         if not stack:
#             break
#         if i == ')':
#             if stack[-1] == '(':
#                 stack.pop()
#                 stack.append(2)
#             elif stack[-1] == '[':
#                 print(0)
#                 exit()
#             else: #숫자인 경우
#                 num = 0
#                 while True:
#                     num += stack.pop()
#                     if not stack:
#                         break
#                     if stack[-1] == '(':
#                         num = num * 2
#                         stack.pop()
#                         stack.append(num)
#                         break
#                     elif stack[-1] == '[':
#                         print(0)
#                         exit()
#
#         elif i == ']':
#             if stack[-1] == '[':
#                 stack.pop()
#                 stack.append(3)
#             elif stack[-1] == '(':
#                 print(0)
#                 exit()
#             else: #숫자인 경우
#                 num = 0
#                 while True:
#                     num += stack.pop()
#                     if not stack:
#                         break
#                     if stack[-1] == '[':
#                         num = num * 3
#                         stack.pop()
#                         stack.append(num)
#                         break
#                     elif stack[-1] == '(':
#                         print(0)
#                         exit()
# rs = True
# for i in ['[',']','(',')']:
#     if i in stack:
#         rs = False
# if rs:
#     print(sum(stack))
# else:
#     print(0)