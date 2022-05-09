# https://selina-park.tistory.com/103
# https://j-ungry.tistory.com/137

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