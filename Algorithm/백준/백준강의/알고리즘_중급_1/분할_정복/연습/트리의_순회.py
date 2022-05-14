# https://sujeng97.tistory.com/6
# 이해하기도 힘들었다..
# post order를 통해 root 노드를 찾고
# root노드는 pre오더의 첫번째 출력 순서이다.
# 인오더를 루트노드를 기준으로 좌우서브트리로 쪼갠다
# 좌우 서브트리에대해 동일 로직을 반복
# 다시풀자
#
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# n = int(input())
# inorder = list(map(int,input().split()))
# postorder = list(map(int,input().split()))
# position = [0]*(n+1)
# for i in range(n):
#     position[inorder[i]] = i
#
# def preorder(istart,iend,pstart,pend):
#     if istart > iend or pstart > pend:
#         return
#
#     root = postorder[pend]
#     print(root,end=' ')
#
#     left_cnt = position[root] - istart
#     right_cnt = iend - position[root]
#
#     preorder(istart,position[root]-1,pstart,pstart+left_cnt-1)
#     preorder(position[root]+1,iend,pend-right_cnt,pend-1)
#
#
# preorder(0,n-1,0,n-1)


# 다시 푼 버전
# 처음부터 짠다고 생각하면 어렵다
# 나중에 복습하자
import sys

sys.setrecursionlimit(int(1e5))
def preorder(istart, iend, pstart, pend):
    #탈출 조건
    if istart > iend or pstart > pend:
        return

    root = postorder[pend]
    print(root, end=' ')

    left_cnt = position[root] - istart
    right_cnt = iend - position[root]

    preorder(istart, position[root]-1, pstart, pstart+left_cnt-1)
    preorder(position[root]+1, iend, pstart+left_cnt, pend-1)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0]*(N+1)
for i in range(N):
    position[inorder[i]] = i
preorder(0, N-1, 0, N-1)