N, M = map(int, input().split())
if N == 1 or M == 1:
    print(1)
elif N < 3:
    print(min(4, (M-1)//2+1))
else:
    if M < 7:
        print(min(4, M))
    else:
        print(M-2)


# 아래 조건은 4 이하만 가능
# elif N < 3:
#     print(min(4, (M-1)//2+1))
# if M < 7:
#     print(min(4, M))