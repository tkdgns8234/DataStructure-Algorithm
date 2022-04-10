# 3. 잃어버린 괄호
# 실패 원리는 알았는데 코딩을 못하겠네 ㅠ 너~~~무 길고 지저분해
# 아래 진행 중 멈춘코드
# 아래 정답코드 있음
# 다시풀자
# from collections import deque
# S = list(input())
#
# # - 가 나오면 다시 - 가 나오기 전까지 괄호 추가
# flag = False
# for i in range(len(S)):
#     if S[i] == '-':
#         if not flag:
#             S.insert(i+1, '(')
#             flag = True
#         else:
#             S.insert(i, ')')
#             flag = False
#     if i == len(S)-1 and flag: # 마지막인데 - 가 나오지 않은경우 ) 추가
#         S.append(')')
#
# temp = 0
# flag = False
# oper = deque()
# result = 0
# num = ''
# for i in S:
#     if i == '-':
#         oper.append(int(num))
#         oper.append(i)
#         num = ''
#     elif i == '+':
#         if flag:
#             temp += int(num)
#             num = ''
#         else:
#             oper.append(int(num))
#             oper.append(i)
#             num = ''
#     elif i == '(':
#         flag = True
#     elif i == ')':
#         flag = False
#         oper.append(temp)
#         temp = 0
#     else:
#         num += i
# # 마지막 num 추가
# oper.append(int(num))
#
# print(oper)

# 정답 코드
# 다시풀자
arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
