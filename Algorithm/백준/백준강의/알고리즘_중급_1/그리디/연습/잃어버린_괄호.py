s = input().split('-')
for i in range(len(s)):
    if '+' in s[i]:
        numbers = s[i].split('+')
        s[i] = sum(map(int, numbers))
    else:
        s[i] = int(s[i])

ans = s[0]
for i in range(1, len(s)):
    ans -= s[i]
print(ans)