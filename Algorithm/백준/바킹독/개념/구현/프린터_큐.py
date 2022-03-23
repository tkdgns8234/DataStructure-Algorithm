# 문제4 프린터 큐
# 너무 억지스럽게 풀었어.. 다시풀자
# 리스트 활용법만 알면 굳이 queue 쓰지 않아도 돼

from collections import deque
for test in range(int(input())):
    n, target = map(int, input().split())
    imp = list(map(int, input().split()))

    data = []
    for i in range(n):
        data.append(((imp[i]), i))
    data = deque(data)

    cnt = 1
    while True:
        is_moved = False
        for i in range(1, n):
            if data[0][0] < data[i][0]:
                val = data.popleft()
                data.append(val)
                is_moved = True
                break

        if not is_moved:
            val = data.popleft()
            if val[1] == target:
                print(cnt)
                break
            cnt += 1
            n -= 1

# 프린터 큐
for test in range(int(input())):
    n, target = map(int, input().split())
    imp = list(map(int, input().split()))
    target_list = [0 for i in range(n)]
    target_list[target] = 1

    cnt = 1
    while True:
        if imp[0] == max(imp):
            if target_list[0] == 1:
                print(cnt)
                break
            else:
                imp.pop(0)
                target_list.pop(0)
            cnt += 1
        else:
            imp.append(imp[0])
            target_list.append(target_list[0])
            imp.pop(0)
            target_list.pop(0)