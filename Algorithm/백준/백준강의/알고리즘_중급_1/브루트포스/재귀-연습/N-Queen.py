# 예전에 한번 풀이를 봤었던 문제
# 다시 봤는데 실패;

# 1. 한 행에 퀸을 놓는다면 동일한 행에 다른 퀸을 놓을 수 없다.
# 2. 퀸은 대각선 이동이 가능하므로 다음 행에서 대각선을 고려하여 퀸을 놓는다

# 대각선 법칙: x1, y1, x2, y2 일때
# abs(x1-x2)   abs(y1-y2) 는 동일하다

def confirm(y, x):
    if x == 0:
        return True
    for i in range(x):
        if abs(row[i] - y) == x - i:
            return False
    return True


def btk(depth):
    global ans
    if depth == N:
        ans += 1
        return

    # 열 탐색
    for i in range(N):
        if not col[i]:
            # 대각선 확인
            if confirm(i, depth):
                row[depth] = i
                col[i] = True
                btk(depth + 1)
                col[i] = False


N = int(input())
col = [False] * N
row = [0] * N
ans = 0
btk(0)
print(ans)