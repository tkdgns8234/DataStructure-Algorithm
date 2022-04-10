# 5. 회전 초밥
# 길이를 구하고, 중복은 x 쿠폰이 길이 안에 없으면 + 1 set 로 관리
# N 접시수 d 초밥의 가짓수 k 연속 접시 수 c 쿠폰
N, d, k, c = map(int, input().split())
data = [int(input()) for _ in range(N)] * 2 # 회전하는 형태로 표현하기 위해

menu_cnt = dict()
menu = set()
end = -1
ans = 0
for start in range(len(data)//2):
    while end - start < k - 1:
        end += 1
        menu.add(data[end])
        menu_cnt[data[end]] = menu_cnt.get(data[end], 0) + 1
    ans = max(ans, len(menu) + 1 if c not in menu else len(menu))

    if menu_cnt[data[start]] <= 1:
        menu.remove(data[start])
    menu_cnt[data[start]] -= 1

print(ans)