# 3. List of Unique Numbers
# [1,2,3,4,5...n] 최대 O(n^2) 보다는 작다
# 처음에 계산했을 때 위 방법이 O(n^2) 가 아닐까 해서 해당 풀이로 풀지 않고 풀이를 참조했는데,
# 이게 되네??/?
# n^2에 가까워보인다고 생각했는데
# 다시 보니 투포인터 유형 자체가 대부분 저런식으로 풀이하고있음 O(N) 에 가까운거였어
# 아래와같은 방식으로(투포인터로) 풀이했을 때 O(n^2)를 O(N) 에 가깝게 풀이할 수 있다고 기억하자

n = int(input())
data = list(map(int, input().split()))
chk = [False] * 100_002

ans = 0
chk[data[0]] = True
en = 0
for start in range(n):
    while en < n-1 and not chk[data[en+1]]:
        en += 1
        chk[data[en]] = True
    ans += (en-start+1)
    chk[data[start]] = False

print(ans)
