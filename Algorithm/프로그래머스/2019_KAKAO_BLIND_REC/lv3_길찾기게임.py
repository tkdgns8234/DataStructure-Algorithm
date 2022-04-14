# 이진탐색트리의 구현 + 순회를 할 수 있는지 묻는 문제다
# 실패
# 다시 푼 코드
# 배운 점
# 이진탐색 트리 + 순회 구현 경험
# 파이썬 class 설계, 활용

# import sys
#
# sys.setrecursionlimit(int(1e9))
# class Node:
#     def __init__(self, idx, x):
#         self.key = idx
#         self.val = x
#         self.left_child, self.right_child = None, None
#
# class Tree:
#     # 루트 노드 초기화
#     def __init__(self, idx, x):
#         node = Node(idx, x)
#         self.root = node
#
#     def insert(self, idx, x):
#         cur_node = self.root
#         while True:
#             if cur_node.val < x:
#                 if cur_node.right_child != None:
#                     cur_node = cur_node.right_child
#                 else:
#                     cur_node.right_child = Node(idx, x)
#                     break
#             else:
#                 if cur_node.left_child != None:
#                     cur_node = cur_node.left_child
#                 else:
#                     cur_node.left_child = Node(idx, x)
#                     break
#
#     def order(self):
#         pre = []
#         post = []
#
#         def ord(node):
#             pre.append(node.key)
#             if node.left_child != None: ord(node.left_child)
#             if node.right_child != None: ord(node.right_child)
#             post.append(node.key)
#
#         ord(self.root)
#         return [pre, post]
#
# def solution(nodeinfo):
#     # 인덱스 번호 추가
#     for i, node in enumerate(nodeinfo):
#         nodeinfo[i] = [i+1] + node
#
#     # y축 좌표 순서로 데이터를 넣어야한다
#     # 그래야 pre, post order가 원하는 결과처럼 나옴
#     nodeinfo.sort(key=lambda x: (x[2]), reverse=True)
#     root_node = nodeinfo[0]
#     tree = Tree(root_node[0], root_node[1])
#
#     for node in nodeinfo:
#         # 루트 노드 제외하고 삽입
#         idx = node[0]
#         x = node[1]
#         if idx == tree.root.key:
#             continue
#         tree.insert(idx, x)
#
#     return tree.order()
#
# print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))












# # 타 블로그 참조
# # 트리 구현
# # 와.. 이거 대단한데?
# # 출처: https: // kyome.tistory.com / 111[KYOME]
# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
#
# class Tree:
#     def __init__(self, dataList):
#         self.data = max(dataList, key=lambda x: x[1])
#         leftList = list(filter(lambda x: x[0] < self.data[0], dataList))
#         rightList = list(filter(lambda x: x[0] > self.data[0], dataList))
#
#         if leftList != []:
#             self.left = Tree(leftList)
#         else:
#             self.left = None
#
#         if rightList != []:
#             self.right = Tree(rightList)
#         else:
#             self.right = None
#
#
# def fix(node, postList, preList):
#     postList.append(node.data)
#     if node.left is not None:
#         fix(node.left, postList, preList)
#
#     if node.right is not None:
#         fix(node.right, postList, preList)
#     preList.append(node.data)
#
#
# def solution(nodeinfo):
#     answer = []
#     root = Tree(nodeinfo)
#     postList = []
#     preList = []
#     fix(root, postList, preList)
#
#     answer.append(list(map(lambda x: nodeinfo.index(x) + 1, postList)))
#     answer.append(list(map(lambda x: nodeinfo.index(x) + 1, preList)))
#     return answer
#
#
#
# # https://velog.io/@akffhaos95/알고리즘-길-찾기-게임
# # 트리 구현
# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
# class Node:
#     def __init__(self, key, x):
#         self.key = key
#         self.x = x
#         self.right, self.left = None, None
#
#
# class Tree:
#     #루트노드 초기화
#     # x 값 기준으로 좌 우 결정됨
#     def __init__(self, head, x):
#         self.head = Node(head, x)
#
#     def insert(self, key, x):
#         cur_node = self.head
#         while True:
#             if cur_node.x > x:  # left down
#                 if cur_node.left == None:
#                     cur_node.left = Node(key, x)
#                     break
#                 else:
#                     cur_node = cur_node.left
#             elif cur_node.x < x:  # right down
#                 if cur_node.right == None:
#                     cur_node.right = Node(key, x)
#                     break
#                 else:
#                     cur_node = cur_node.right
#
#     def preorder(self):
#         res = []
#
#         def order(node):
#             nonlocal res
#             res.append(node.key)
#             if node.left != None: order(node.left)
#             if node.right != None: order(node.right)
#
#         order(self.head)
#         return res
#
#     def postorder(self):
#         res = []
#
#         def order(node):
#             nonlocal res
#             if node.left != None: order(node.left)
#             if node.right != None: order(node.right)
#             res.append(node.key)
#
#         order(self.head)
#         return res
#
#
# def solution(nodeinfo):
#     answer = []
#     for i in range(len(nodeinfo)):
#         nodeinfo[i] = [i + 1] + nodeinfo[i]
#
#     nodeinfo.sort(key=lambda x: (x[2]), reverse=True)
#
#     tree = Tree(nodeinfo[0][0], nodeinfo[0][1])
#
#     for i in nodeinfo[1:]:
#         tree.insert(i[0], i[1])
#
#     answer.append(tree.preorder())
#     answer.append(tree.postorder())
#     return answer
#
# # https://wiselog.tistory.com/103
# # 1. nodeinfo의 각 원소(x,y위치)에 노드번호(인덱스+1)를 추가한다.
# #    (Java의 경우, Node 클래스를 만들어 필드로 x위치, y위치, 노드번호를 갖도록 한다.
# #     이 Node를 저장하는 ArrayList를 생성한다.)
# # 2. nodeinfo를 x를 기준으로 오름차순 정렬한 arrX, y를 기준으로 내림차순 정렬한 arrY를 생성한다.
# # 3. 전위순회하는 함수 preorder, 후위순회하는 함수 postorder를 정의한다.
# # 4. preorder의 매개변수로 arrX, arrY, 답을 저장할 배열 answer을 받는다.
# # 5. 중심이 될 노드 node=arrY[0]을 선언한다. (y축값이 제일 높은 노드가 루트이므로)
# #    중심 노드의 arrX에서의 인덱스를 알아낸다. (idx)
# #    중심 노드를 기준으로 왼쪽 노드들을 저장할 arrY1, 오른쪽 노드들을 저장할 arrY2를 준비한다.
# # 6. arrY에서 중심노드를 제외한 인덱스 1~마지막까지 탐색한다.(i)
# #   6-1. arrY[i]의 x값이 중심노드의 x값보다 작다면 arrY1에 삽입, 크다면 arrY2에 삽입한다.
# # 7. 답을 저장하는 answer에 중심노드의 번호인 node[2]를 삽입한다.
# # 8. 만약 arrY1의 크기가 0이 아니라면 arrY1과 arrX의 0부터 idx까지로 다시 preorder를 재귀호출한다.
# # 9. 만약 arrY2의 크기가 0이 아니라면 arrY2와 arrX의 idx+1부터 끝까지로 다시 preorder를 재귀호출한다.
# # 10. 후위순회 postorder도 똑같지만 7,8,9번의 순서를 후위순회 순서인 8,9,7로 바꾼다.
#
#
# import sys
# sys.setrecursionlimit(10 ** 6)
#
# def preorder(arrY, arrX, answer):
#     node = arrY[0]
#     idx = arrX.index(node)
#     arrY1 = []
#     arrY2 = []
#
#     for i in range(1, len(arrY)):
#         if node[0] > arrY[i][0]:
#             arrY1.append(arrY[i])
#         else:
#             arrY2.append(arrY[i])
#
#     answer.append(node[2])
#     if len(arrY1) > 0:
#         preorder(arrY1, arrX[:idx], answer)
#     if len(arrY2) > 0:
#         preorder(arrY2, arrX[idx + 1:], answer)
#     return
#
#
# def postorder(arrY, arrX, answer):
#     node = arrY[0]
#     idx = arrX.index(node)
#     arrY1 = []
#     arrY2 = []
#
#     for i in range(1, len(arrY)):
#         if node[0] > arrY[i][0]:
#             arrY1.append(arrY[i])
#         else:
#             arrY2.append(arrY[i])
#
#     if len(arrY1) > 0:
#         postorder(arrY1, arrX[:idx], answer)
#     if len(arrY2) > 0:
#         postorder(arrY2, arrX[idx + 1:], answer)
#     answer.append(node[2])
#     return
#
#
# def solution(nodeinfo):
#     preanswer = []
#     postanswer = []
#
#     for i in range(len(nodeinfo)):
#         nodeinfo[i].append(i + 1)
#
#     arrY = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
#     arrX = sorted(nodeinfo)
#
#     preorder(arrY, arrX, preanswer)
#     postorder(arrY, arrX, postanswer)
#
#     return [preanswer, postanswer]