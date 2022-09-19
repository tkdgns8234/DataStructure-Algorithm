N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))  # + - * / 순서

max_val = -int(1e10)
min_val = int(1e10)


def btk(depth, total):
    global min_val, max_val
    if depth == N:
        min_val = min(min_val, total)
        max_val = max(max_val, total)

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                temp = total + numbers[depth]
            elif i == 1:
                temp = total - numbers[depth]
            elif i == 2:
                temp = total * numbers[depth]
            else:
                if total < 0:
                    temp = -(-total // numbers[depth])
                else:
                    temp = total // numbers[depth]

            btk(depth + 1, temp)
            op[i] += 1


btk(1, numbers[0])
print(max_val, min_val, sep="\n")
