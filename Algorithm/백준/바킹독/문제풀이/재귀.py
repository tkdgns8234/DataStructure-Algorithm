# 1. 재귀함수가 뭔가요?
# import sys
# sys.setrecursionlimit(51)
# n = int(input())
#
# def reculsive(num, depth):
#     c = '____' * (num - (num-depth))
#     print(c + "\"재귀함수가 뭔가요?\"", sep="")
#     if depth == num:
#         print(c + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
#         print(c + "라고 답변하였지.")
#         return
#     print(c + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
#     print(c + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#     print(c + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
#     reculsive(num, depth + 1)
#     print(c + "라고 답변하였지.")
#
# print('''어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# \"재귀함수가 뭔가요?\"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."''')
# reculsive(n,1)
# print("라고 답변하였지.")

# 2. 종이의 개수
# 잘 풀었지만 메모리, 시간을 너무 잡아먹어
# 좀 더 효율적으로 작성할 수 있어
# 3000ms 소요

# import sys
# sys.setrecursionlimit(3**10)
# input = sys.stdin.readline
# FALSE = -100
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
#
# def check(arr):
#     pivot = arr[0][0]
#     row = len(arr)
#     col = len(arr[0])
#     for i in range(row):
#         for j in range(col):
#             if arr[i][j] != pivot:
#                 return FALSE  # 같지 않음
#     return pivot
#
# def reculsive(data):
#     val = check(data)
#     if val != FALSE:
#         result.append(val)
#         return
#     else:
#         length = len(data)
#         for i in range(0, length, length//3):
#             for j in range(0, length, length//3):
#                 reculsive([row[j:j+length//3] for row in data[i:i+length//3]])
#
#
# result = []
# reculsive(data)
# print(result.count(-1))
# print(result.count(0))
# print(result.count(1))

# 종이의 개수
# 효율적인 코드
# 1400ms 소요
# import sys
#
# result = [0, 0, 0]
# paper = []
#
#
# def checkPaper(rs, cs, n):
#     check = False
#     compare = paper[rs][cs]
#     for i in range(rs, rs + n):
#         for j in range(cs, cs + n):
#             if paper[i][j] != compare:
#                 check = True
#                 break
#         if check:
#             break
#     if check:
#         next = n//3
#         for i in range(3):
#             for j in range(3):
#                 checkPaper(rs + next * i, cs + next * j, next)
#     else:
#         result[int(compare)] += 1
#         return
#
#
# def main():
#     n = int(sys.stdin.readline())
#     for _ in range(n):
#         paper.append(list(sys.stdin.readline().split()))
#     checkPaper(0, 0, n)
#     print(result[-1])
#     print(result[0])
#     print(result[1])
#
#
# main()

# 3. 색종이 만들기
# 위문제와 거의 동일하다
# 효율적으로 풀어내보자
# 성공!
# import sys
# input = sys.stdin.readline
# result = [0, 0] #흰색, 파란색
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
#
# def check(x, y, next):
#     pivot = data[x][y]
#     for i in range(x, x+next):
#         for j in range(y, y+next):
#             if data[i][j] != pivot:
#                 return False
#     return True
#
# def reculsive(x, y, next):
#     rs = check(x, y, next)
#     if rs:
#         result[data[x][y]] += 1
#     else:
#         n_next = next//2
#         for i in range(2):
#             for j in range(2):
#                 reculsive(x + n_next*i, y + n_next*j, n_next)
# reculsive(0, 0, n)
# print(f'{result[0]}\n{result[1]}')

# 4. 쿼드트리
# import sys
# input = sys.stdin.readline
# n = int(input())
# data = [list(map(int, list(input().rstrip()))) for _ in range(n)]
# result = []
#
# def check(x, y, next):
#     pivot = data[x][y]
#     for i in range(x, x+next):
#         for j in range(y, y+next):
#             if data[i][j] != pivot:
#                 return False
#     return True
#
# def reculsive(x, y, next):
#     c = check(x, y, next)
#     if c:
#         result.append(data[x][y])
#     else:
#         n_next = next//2
#         result.append('(')
#         for i in range(2):
#             for j in range(2):
#                 reculsive(x + n_next*i, y + n_next*j, n_next)
#         result.append(')')
#
# reculsive(0, 0, n)
# print(*result, sep="")

# 좀 더 효울적이고 좋아보이는 코드
# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
#
# k = int(input().strip())
# lines = [input() for _ in range(k)]
# video = [[i for i in line] for line in lines]
#
#
# def solve(n, x, y):
#     if n == 1:
#         return video[y][x]
#     h = int(n/2)
#     a = solve(h, x, y)
#     b = solve(h, x+h, y)
#     c = solve(h, x, y+h)
#     d = solve(h, x+h, y+h)
#     if all(map(lambda r: r == "1", [a, b, c, d])):
#         return "1"
#     if all(map(lambda r: r == "0", [a, b, c, d])):
#         return "0"
#     return f"({a}{b}{c}{d})"
#
#
# print(solve(k, 0, 0))

# 5. 별 찍기 - 10
# 아래 방법 좋은데, 배열이 너무많아져 4차원,6차원... 값을 어떻게 찍을지도 문제다
# 풀이를 찾아보자..
# 아래 코드는 실패
# 다시풀자
# n = int(input()) # 3
#
# def reculsive(num):
#     if num == 1:
#         return '*'
#     priv = reculsive(num//3)
#     arr = []
#     for i in range(3):
#         arr.append([])
#         for j in range(3):
#             if num//3 <= i < num//3*2:
#                 if num//3 <= j < num//3*2:
#                     arr[-1].append(' ')
#                     continue
#             arr[-1].append(priv)
#     return arr
#
# print(reculsive(n))
# # rs = reculsive(n)

# 배열을 미리 선언해두고 대입할까?
# 실패. 풀이를 보자 아래 링크 참조
# 출처: https://cotak.tistory.com/38 [TaxFree]
# 풀이1
# import sys
# sys.setrecursionlimit(10**6)
# def paint_star(LEN):
#     DIV3 = LEN//3
#     if LEN == 3:
#         g[1] = ['*', ' ', '*']
#         g[0][:3] = g[2][:3] = ['*']*3
#         return
#
#         paint_star(DIV3)
#
#         for i in range(0, LEN, DIV3):
#             for j in range(0, LEN, DIV3):
#                 if i != DIV3 or j != DIV3:
#                     for k in range(DIV3):
#                         g[i+k][j:j+DIV3] = g[k][:DIV3]
#
# n = int(sys.stdin.readline().strip())
# g = [[' ' for _ in range(n)] for _ in range(n)]
# paint_star(n)
#
# for i in range(n):
#     for j in range(n):
#         print(g[i][j], end='')
#     print()

# 풀이2
# 내가 풀었던 코드와 매우 유사해
# 비교해보자

# import sys
# sys.setrecursionlimit(10**6)
# def append_star(LEN):
#     if LEN == 1:
#         return ['*']
#     Stars = append_star(LEN//3)
#     L = []
#
#     for S in Stars:
#         L.append(S*3)
#     for S in Stars:
#         L.append(S+' '*(LEN//3)+S)
#     for S in Stars:
#         L.append(S*3)
#     return L
#
# n = int(sys.stdin.readline().strip())
# print(append_star(n))
# # print('\n'.join(append_star(n)))

# 별찍기 - 11
# 오우.. disgusting
# 다시풀기
# 해설 참조
# def print_star(x, y, n):
#     if n == 3:
#         ans[x][y] = '*'
#         ans[x+1][y-1] = ans[x+1][y+1] = '*'
#         for i in range(-2, 3):
#             ans[x+2][y+i] = '*'
#     else:
#         nn = n // 2
#         print_star(x, y, nn)
#         print_star(x+nn, y-nn, nn)
#         print_star(x+nn, y+nn, nn)
#
#
# N = int(input())
# ans = [[' '] * 2 * N for _ in range(N)]
#
# print_star(0, N-1, N)
# for row in ans:
#     print("".join(row))