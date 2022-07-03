
T_E, T_S, T_M = map(int, input().split())

ans = e = s = m = 0

while True:
    ans += 1
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    if e == T_E and s == T_S and m == T_M:
        break
print(ans)
