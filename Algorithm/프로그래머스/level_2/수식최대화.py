# 실패
# lve2 치고 어렵다
# 현타가 세게 온다..

# 풀이는 두가지 방법이 존재한다
# stack + 반복문
# 분할정복+재귀
# 두가지 형태로 풀어보자

from itertools import permutations

def oper(a, b, op):
    a, b = map(int, [a, b])
    if op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '+':
        return a+b

def solve(op, exp):
    # 표현식 쪼개기
    arr = []
    temp = ''
    for e in exp:
        if str(e).isnumeric():
            temp += e
        else:
            arr.append(int(temp))
            arr.append(e)
            temp = ''
    arr.append(int(temp))

    for o in op:
        stack = []
        while arr:
            v = arr.pop(0)
            if v == o:
                stack.append(oper(stack.pop(), arr.pop(0), o))
            else:
                stack.append(v)
        arr = stack
    return int(arr[0])


def solution(expression):
    answer = 0
    for op in permutations(['+','*','-'], 3):
        answer = max(answer, abs(solve(op, expression)))
    return answer

solution("100-200*300-500+20")



# 분할정복 + 재귀 풀이
# https://haeseok.medium.com/프로그래머스-수식-최대화-eaa534d55316
# from itertools import permutations
# def calc(priority, n, expression):
#     print(n, expression, priority)
#     if n == 2:
#         return str(eval(expression))
#     if priority[n] == '*':
#         res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
#     if priority[n] == '+':
#         res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
#     if priority[n] == '-':
#         res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
#     return str(res)
#
#
# def solution(expression):
#     answer = 0
#     for op in permutations(['+','*','-'], 3):
#         answer = max(answer, abs(int(calc(op, 0, expression))))
#         print('-----answer=',answer)
#     return answer
#
# v  = solution("100-200*300-500+20")
# print(v)

# 고난도풀이
# def solution(expression):
#     operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
#     answer = []
#     for op in operations:
#         a = op[0]
#         b = op[1]
#         temp_list = []
#         for e in expression.split(a):
#             temp = [f"({i})" for i in e.split(b)]
#             temp_list.append(f'({b.join(temp)})')
#         answer.append(abs(eval(a.join(temp_list))))
#     return max(answer)
#
#
# solution("100-200*300-500+20")