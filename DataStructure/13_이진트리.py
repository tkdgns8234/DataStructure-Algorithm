# 배열 or 리스트로 이진트리를 만드는 방법은 저장공간의 효율성이 떨어질 수 있음
# => Node 를 실제 구현해서 만드는 방법이 있음
# 이진트리의 순회 

#   M
# L   R

# order 는 다 부모노드 기준
# preorder   M L R
# inorder    L M R
# postorder  L R M

# 이진트리의 순회 방법


class Node:
    def __init__(self, key = None):
        self.key = key
        self.left, self.right, self.parent = None, None, None
    
    def preorder(self):
        if self:
            print(self.key)
        
        if self.left:
            self.preorder(self.left)
        
        if self.right:
            self.preorder(self.right)
    
    #inorder, post order의 경우 print 문 위치만 바꾸면 된다 (재귀적 호출)
        