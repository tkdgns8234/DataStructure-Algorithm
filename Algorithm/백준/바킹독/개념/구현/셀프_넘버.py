# 문제3 셀프 넘버
# 셀프넘버가 아닌것 추가
def d(n):
    n = n + sum(map(int, str(n)))
    return n

not_self_num = []
for i in range(1, 10001):
    not_self_num.append(d(i))

for i in range(1, 10001):
    if i not in not_self_num:
        print(i)