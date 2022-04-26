# 연산자 갯수는 초과되도 상관 없다
# 단지, 10개를 끼워넣을 수 있는 모든 경우의 수를 탐색하기만 하면 된다

n = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))

def btk(depth, oper, total):
    global max_val, min_val

    if depth == n-1:
        min_val = min(min_val, total)
        max_val = max(max_val, total)
        return

    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            if i == 0:
                btk(depth + 1, oper, total+numbers[depth+1])
            if i == 1:
                btk(depth + 1, oper, total-numbers[depth+1])
            if i == 2:
                btk(depth + 1, oper, total * numbers[depth + 1])
            if i == 3:
                if total < 0:
                    btk(depth + 1, oper, -(-total // numbers[depth + 1]))
                else:
                    btk(depth + 1, oper, total // numbers[depth + 1])
            oper[i] +=1

min_val = int(1e11)
max_val = -int(1e11)
btk(0, operations, numbers[0])
print(max_val)
print(min_val)