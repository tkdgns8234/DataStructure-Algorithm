# 실패
# 나중에 다시 풀자

# 문제 해설
# https://hongjw1938.tistory.com/180
# 시간복잡도: https://nicotina04.tistory.com/33
# 시간복잡도도 최대 4억인데 문제 자체가 난해하네,, 6초에 4억연산이 가능한가

# 비트마스크를 활용한 방법인데
# 비트마스크가 익숙지 않다 ㅠ 어떻게 이런 방법을 사용하는건지,,

# 비트마스크를 통해 부분집합을 구하는 유형이었다.
# 아래 블로그 참조
# https://selina-park.tistory.com/103
# https://j-ungry.tistory.com/137
# 맨 아래 코드부분 예제 확인하고 다시 보면 훨씬 이해가 잘 될거다

n = int(input())
coin = [list(input()) for _ in range(n)]
ans = n * n + 1

print(1<<n)
for bit in range(1 << n):
    tmp = [coin[i][:] for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'

    tot = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T':
                cnt += 1
        tot += min(cnt, n-cnt)
    ans = min(ans, tot)

print(ans)



# 비트마스크를 통해 부분집합을 구하는 예제
# 아! 깨닳았다
arr = [3,6]
n = len(arr)
# 이진수 11 은 100 보다 1 작은 수 이므로
# 1<<2 해서 100까지 돌게 만듬
# n은 곧 원소의 갯수와 같음
for i in range(1<<n):
    for j in range(n):
        # 이부분이 예를들어 i가 이진수로11 일때 각 원소의 위치가 1인지 확인하는 부분이구나
        # & 연산을 사용하니까
        # 원소의 갯수-1 만큼 j 이동
        if i&(1<<j):
            print(arr[j], end=" ")
    print()