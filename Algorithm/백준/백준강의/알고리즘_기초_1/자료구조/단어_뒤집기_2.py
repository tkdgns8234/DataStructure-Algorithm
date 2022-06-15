words = input()
stack = []
answer = []
flag = False
for w in words:
    if w == '<':
        flag = True
        answer += stack[::-1]
        stack.clear()
        answer += w
        continue
    elif w == '>':
        flag = False
        answer += w
        continue
    elif w == " ":
        answer += stack[::-1]
        stack.clear()
        answer += w
        continue

    if flag:
        answer += w
    else:
        stack.append(w)

print(''.join(answer + stack[::-1]))