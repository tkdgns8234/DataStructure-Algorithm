# 4. 주식
# 가장 큰 값을 찾고 그 앞에있는 값들을 모두 산 후 큰값인 날에 판다
# list 가 0 이될떄까지 반복한다
# -> 시간복잡도 안될거같은데
# O(n) 또는 Log(n) 시간내에 해결하지 않으면 불가하다

# 뒤에서부터 계산하는게 max 값을 찾지 않아도 된다. 훨씬 효율적이네,

T = int(input())
for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))

    result = 0
    m = int(-1e9)
    for i in range(len(data)-1, -1, -1):
        if m > data[i]:
            result += m - data[i]
        else:
            m = data[i]
    print(result)
