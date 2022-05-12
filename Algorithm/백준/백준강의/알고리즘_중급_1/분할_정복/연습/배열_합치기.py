N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rs = []
a, b = 0, 0
while a < len(A) and b < len(B):
    if A[a] < B[b]:
        rs.append(A[a])
        a += 1
    else:
        rs.append(B[b])
        b += 1
rs += A[a:]
rs += B[b:]
print(*rs, sep=" ")
