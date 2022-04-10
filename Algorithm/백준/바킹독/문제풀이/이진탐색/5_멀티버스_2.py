# 5. 멀티버스 2
# 좌표압축 문제인데 이진탐색 방법이 아닌 dictionary 를 이용해서 푸는 방법이 있다
# 이게 더 간단해보이는데 해보자
M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]

new_data = [[] for _ in range(M)]
dict = {}
for i in range(len(data)):
    # !!!!!주의!!!!! set 사용 시, 순서가 바뀔 수 있음, 위 data 에서 set 으로 중복 제거 시 원하는 답 도출 불가
    temp = sorted(list(set(data[i])))
    for j in range(len(temp)):
        dict[temp[j]] = j
    for j in data[i]:
        new_data[i].append(dict[j])

cnt = 0
for i in range(0, M-1):
    for j in range(i, M):
        if i == j:
            continue
        if new_data[i] == new_data[j]:
            cnt += 1

print(cnt)
