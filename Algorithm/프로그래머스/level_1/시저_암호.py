
def solution(s, n):
    answer = ''
    for i in s:
        if i.isspace():
            answer += ' '
            continue
        next = ord(i) + n
        if ord('A') <= ord(i) <= ord('Z'):
            if next > ord('Z'):
                next = ord('A') + (next - ord('Z')) - 1
        elif ord('a') <= ord(i) <= ord('z'):
            if next > ord('z'):
                next = ord('a') + (next - ord('z')) - 1
        answer += chr(next)
    return answer

print(solution("a B z", 4))

# 더 좋은 풀이
# 26 (a와 z의 차이값을 이용하는게 포인트)
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)