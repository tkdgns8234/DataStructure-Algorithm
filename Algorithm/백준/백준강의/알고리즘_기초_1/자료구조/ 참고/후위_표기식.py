# 중위 표기법을 후위 표기법으로 바꾸는 과정은 다음과 같다.
#
# 피연산자가 들어오면 바로 출력한다.
# 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것들을 빼고 자신을 스택에 담는다.
# 여는 괄호를 만나면 무조건 스택에 담는다.
# 닫는 괄호를 만나면 여는 괄호를 만날때 까지 스택에서 출력한다.
# 이를 코드로 표현하면 아래와 같다.

data = input()
stack = []
answer = ''
for i in data:
    if i.isalpha():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
print(answer + ''.join(stack[::-1]))
