# ez
# 시뮬레이션 유형
# 문제에서 설명하는데로 풀어나가면 됨

def devide_str(p):
    u, v = '', ''
    left_count, right_count = 0, 0
    for w in p:
        if w =='(':
            left_count += 1
        else:
            right_count += 1
        if left_count != 0 and left_count == right_count:
            u = p[:left_count+right_count]
            v = p[left_count+right_count:]
            return u, v
    return u, v

def confirm(u):
    stack = []
    for w in u:
        if w == '(':
            stack.append('(')
        elif w == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return True


def solution(p):
    # 1
    if p == "": return p

    # 2 두 균형 문자열로 분할
    u, v = devide_str(p)
    # u가 올바른 문자열인지
    if confirm(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for word in u[1:-1]:
            if word == '(':
                answer += ')'
            else:
                answer += '('
        return answer

v = solution("))((")
print(v)