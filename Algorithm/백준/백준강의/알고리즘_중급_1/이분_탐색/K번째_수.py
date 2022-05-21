# 아이디어가 떠오르지 않아 풀이 방법을 참조했다.
# 파라메트릭 서치 유형 문제
# B[k]를 구해야 하는 문제
# 특정 숫자(N)를 정하고 해당 숫자가 k번째에 위치해 있는지 확인하는 방법으로 풀어나간다
# 특정 숫자(N)가 몇번째 위치에 있는지 확인하는 방법
# -> 각 행마다 N 이하 수의 갯수를 확인
# https://kbw1101.tistory.com/29 참조

# 연산 횟수가 매우 많은 경우
# 파라메트릭 서치 방법을 사용하면 다양한 방법으로 문제를 풀이할 수 있구나!


def get_position(num):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, num//i)
    return cnt

def binary_search(start, end):
    global ans
    while start <= end:
        mid = (start+end)//2

        p = get_position(mid)
        if p < K:
            start = mid + 1
        else:
            ans = min(ans, mid)
            end = mid - 1

N = int(input())
K = int(input())
ans = int(1e10)
binary_search(1, N**2)
print(ans)
