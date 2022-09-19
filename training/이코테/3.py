zero_cnt = 0
one_cnt = 0

before_val = -1

num = input()
for i in num:
    if i == "1":
        if before_val != 1:
            one_cnt += 1

    if i == "0":
        if before_val != 0:
            zero_cnt += 1

    before_val = int(i)

print(min(zero_cnt,one_cnt))