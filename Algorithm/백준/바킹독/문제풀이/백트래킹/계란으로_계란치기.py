# 14. 계란으로 계란치기
# 푸는데 시간이 걸렸지만 스스로 해냈다
# 너무 잘했다 ^_^ 시간복잡도도 잘 나와
import sys
input = sys.stdin.readline
def btk(depth, arr):
    global max_val
    if depth == n:
        c = 0
        for i in range(n):
            if arr[i][0] <= 0:
                c += 1
        max_val = max(c, max_val)
        return

    armor, weight = arr[depth][0], arr[depth][1]
    if armor < 0:
        btk(depth + 1, arr)  # 집은 계란이 꺠졌으면 다음 계란으로 넘어간다
        return

    hit = False
    for i in range(n):
        if i == depth or arr[i][0] <= 0:
            continue  # 자기 자신은 치지 않는다, 타겟의 내구도가 0 보다 크면
        hit = True
        armor_i, weight_i = arr[i][0], arr[i][1]
        # 치기
        arr[depth][0] = armor - weight_i
        arr[i][0] = armor_i - weight
        btk(depth + 1, arr)
        # 복구
        arr[depth][0] = armor
        arr[i][0] = armor_i

    if not hit: #나머지가 다 깨졌으면 치지 않고 넘어간다
        btk(depth + 1, arr)


n = int(input())
data = []  # 내구도 / 무게
for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    data.append([temp[0], temp[1]])

max_val = 0
btk(0, data)
print(max_val)