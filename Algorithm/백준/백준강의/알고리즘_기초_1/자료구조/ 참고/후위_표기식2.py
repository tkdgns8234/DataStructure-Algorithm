N = int(input())
data = input()
mapped_value = [input() for _ in range(N)]

stack = []
for d in data:
    if d.isalpha():
        num = mapped_value[ord(d)-ord('A')]
        stack.append(num)
    else:
        a = stack.pop()
        b = stack.pop()
        r = eval(str(b)+d+str(a))
        stack.append(r)

print("{:.2f}".format(stack[-1]))