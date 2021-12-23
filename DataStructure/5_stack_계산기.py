# infix -> postfix 로 변경
# 계산

# 1. 피연산자의 순서는 그대로
# 2. 연산자 스택에 담으면서 비교 후 pop
# (: 우선순위 가장 낮음 ):우선순위 가장 높음
# (는 )가 나올때까지 대기 후 다 빼냄
#  +,-,/,* 중 우선순위 자기보다 높은애가 존재하면 다 빼냄

# 계산도 스택 이용 연산자 나왔을 때 스택에 쌓인 숫자 연산 후 push
import sys

class Stack:
    def __init__(self):
        self.store = list()

    def push(self, val):
        self.store.append(val)

    def pop(self):
        try:
            return self.store.pop()
        except IndexError as e:
            print(e)

    def top(self):
        try:
            return self.store[-1]
        except IndexError as e:
            print(e)

    def __len__(self):
        return len(self.store)

def seperate_string(input):
    l = list()
    s = ""
    for word in input:
        if word in "-+/*()":
            if s != "":
                l.append(s)
            l.append(word)
            s = ""
        else:
            s += word
    if s != "":
        l.append(s)
    print(l)
    return l

# 후위연산으로변경 후 return 함수 만들자
def postfix(input):
    stack = Stack()
    post_string = list()

    for word in list(seperate_string(input)):
        if word == "(":
            stack.push(word)
        elif word == ")":
            while True:
                if len(stack) != 0 and stack.top() == "(":
                    stack.pop()
                    break
                post_string.append(stack.pop())
        elif word in "+-*/":
            if word in "+-":
                if len(stack) != 0 and stack.top() in "/*":
                    for i in range(len(stack)):
                        post_string.append(stack.pop())
                stack.push(word)
            else:
                #incaseof /*
                stack.push(word)
        else:
            post_string.append(word)
    for i in range(len(stack)):
        post_string.append(stack.pop())

    print("post format string = {}".format(post_string))
    return post_string


input_string = sys.stdin.readline().strip()
post_string = postfix(input_string)
stack = Stack()
for i in post_string:
    if i in "+-/*":
        word2 = float(stack.pop())
        word1 = float(stack.pop())
        result = 0
        if i == "+":
            result = word1 + word2
        elif i == "-":
            result = word1 - word2
        elif i == "*":
            result = word1 * word2
        elif i == "/":
            result = word1 / word2
        stack.push(result)
    else:
        stack.push(i)
result = stack.pop()

print("입력하신 {} 연산의 결과는 {} 입니다".format(input_string, result))

# 어려웠던점:
# 1. 형변환 잘 하기
# 2. list += 연산으로 string을 넣으면 분리해서 들어가는것
# 3. exception 발생 (top, pop 시, stack 크기 0보다큰지 확인)