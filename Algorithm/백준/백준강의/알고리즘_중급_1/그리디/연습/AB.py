# 실패
# 다시풀기
# 어렵다..
# 그리디도 꼬아서 내면 난이도가 산으로 간다

# 아이디어만 떠올리면 간단한 문제였어.,,
# B를 깔아놓고 A의 위치를 왼쪽으로 한칸씩 밀어 푸는 문제
# BBBBA  -> 0
# BBBAB -> 1
# ABBBB -> 4
# ABBAB -> 4
# ABABB -> 5

N, K = map(int, input().split())
S = ['B']*N
cnt = 0
# 절반 이상 A로 바꾸는 경우 숫자가 줄어들기 때문에 절반 이상 탐색할 필요가 없음
for j in range(N//2):
    # 'A'가 하나 추가되는 경우 이미 필드에 추가된 'A'의 갯수만큼 -1 시킨다.
    cnt -= j
    for i in range(N-1, -1+j, -1):
        # 뒤에서 2번째 위치로 들어간 경우부터 cnt 증가시키고, 다음 인덱스를 B로 바꿈
        if i < N-1:
            S[i+1] = 'B'
            cnt += 1
        S[i] = 'A'
        if cnt == K:
            print(''.join(S))
            exit(0)
print(-1)