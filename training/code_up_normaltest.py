#코드업 바둑알 문제
# 배열 미리 초기화 문제, 코어부분

# SIZE = 19
# B = list()

# for i in range(SIZE):
#     B.append(list(map(int, input().split())))

# num = int(input())
# for i in range(num):
#     x,y = map(int, input().split())
#     for j in range(1, 20):
#         B[x-1][j-1] = 1 if B[x-1][j-1]==0 else 0
#         B[j-1][y-1] = 1 if B[j-1][y-1]==0 else 0
                
# for i in range(1, 20):
#     for j in range(1, 20):
#         print(B[i-1][j-1], end=" ")
#     print()


#코드업 설탕과자뽑기
# 배열인덱스 -1접근과 for문중복돌릴때 가로세로 잘 확인 len(L) 같은거
# h,w = map(int, input().split())
# L = [[0 for _ in range(w)] for _ in range(h)]

# n = int(input())
# for i in range(n):
#     l,d,x,y = map(int, input().split())
#     for _ in range(l):
#         if d == 0:
#             L[x-1][y-1] = 1
#             y+=1
#         elif d == 1:
#             L[x-1][y-1] = 1
#             x+=1
        
# for i in range(len(L)):
#     for j in range(len(L[0])):
#         print(L[i][j], end=" ")
#     print()

#코드업 last 개미문제
L = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    L[i] = list(map(int, input().split()))

cpx = 1
cpy = 1
L[1][1] = 9
while True:
    if L[cpx][cpy+1] != 1:
        if L[cpx][cpy+1] == 2:
            L[cpx][cpy+1] = 9
            break;
        cpy += 1
        L[cpx][cpy] = 9
    else:
        if L[cpx+1][cpy] != 1:
            if L[cpx+1][cpy] == 2:
                L[cpx+1][cpy] = 9
                break;
            cpx += 1
            L[cpx][cpy] = 9
        else:
            break;
    

    
for i in range(10):
    for j in range(10):
        print(L[i][j], end=" ")
    print()