# 이미 푼 문제
# 실패 반성하자
# 반복문으로 분할하는게 생각보다 쉽지 않은문제다;

# import sys
#
# def solve(paper):
#     global cnt
#     paper_len = len(paper)
#     if paper_len == 1:
#         cnt[paper[0][0]+1]
#         return
#     if confirm(paper):
#         val = paper[0][0]
#         cnt[val+1]
#     else:
#         split = paper_len//3
#         temp = [[0]*split for _ in range(split)]
#         for i in range(0, paper_len, split):
#             for j in range(3):
#                 temp[0][j] = paper[i][i+j]
#                 temp[1][j] = paper[i+1][i + j]
#                 temp[2][j] = paper[i+2][i + j]
#         solve(temp)
#
#
# def confirm(paper):
#     p = paper[0][0]
#     for i in range(len(paper)):
#         for j in range(len(paper)):
#             if p != paper[i][j]:
#                 return False
#     return True
#
# input = sys.stdin.readline
# N = int(input())
# paper = [list(map(int, input().split())) for _ in range(N)]
# cnt = [0]*3
#
# solve(paper)
# print(*cnt, end="\n")


# 재풀이 1 (옛날에 풀었던 방식)
# import sys
#
# def solve(paper):
#     global cnt
#     paper_len = len(paper)
#     if confirm(paper):
#         val = paper[0][0]
#         cnt[val+1] += 1
#     else:
#         split = paper_len//3
#         for i in range(0, paper_len, split):
#             for j in range(0, paper_len, split):
#                 solve([i[j:j+split] for i in [row for row in paper[i:i+split]]])
#
#
# def confirm(paper):
#     p = paper[0][0]
#     for i in range(len(paper)):
#         for j in range(len(paper)):
#             if p != paper[i][j]:
#                 return False
#     return True
#
# input = sys.stdin.readline
# N = int(input())
# paper = [list(map(int, input().split())) for _ in range(N)]
# cnt = [0]*3
#
# solve(paper)
# print(*cnt, sep="\n")



# 재풀이 2 다른 사람들이 주로 풀이하는 방식
# 배열을 계속 넘기는건 메모리 낭비가 심하다
# 위치를 넘기는 방식
import sys

def solve(x, y, s):
    global cnt
    num = paper[x][y]
    for i in range(x, x+s):
        for j in range(y, y+s):
            if paper[i][j] != num:
                for a in range(x, x+s, s//3):
                    for b in range(y, y+s, s//3):
                        solve(a, b, s//3)
                return
    cnt[num+1] += 1


input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0]*3

solve(0, 0, N)
print(*cnt, sep="\n")