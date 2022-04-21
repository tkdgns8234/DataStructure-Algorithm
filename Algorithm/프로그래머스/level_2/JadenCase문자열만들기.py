def solution(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0 or s[i-1] == ' ':
            if s[i].isalpha():
                s[i] = s[i].upper()
        else:
            if s[i].isalpha():
                s[i] = s[i].lower()

    answer = ''.join(s)
    return answer

v = solution("3people unFollowed me")
print(v)