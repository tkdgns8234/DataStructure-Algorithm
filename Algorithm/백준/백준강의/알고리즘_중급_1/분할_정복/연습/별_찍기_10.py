# 실패
# 재귀.. 어렵다
# 다시풀자..

# 정답 코드를 보고 다시 작성해본 코드
# 재귀, 분할정복 방식, 큰 문제를 작은 문제로 쪼개서 푸는건데
# 큰문제를 통으로 생각해서 풀려고하면 힘들다
# 재귀적 구조가 보이면 일단 작은것부터 해결하는데 집중해보자

def dfs(depth):
  if depth == 1:
    return ['*']

  star = dfs(depth//3)
  temp_star = []
  for s in star:
    temp_star.append(s*3)
  for s in star:
    temp_star.append(s+' '*(depth//3)+s)
  for s in star:
    temp_star.append(s*3)
  return temp_star

N = int(input())
rs = dfs(N)
print(*rs, sep="\n")