# circulary linked list 원형 리스트 라고도 부름
# 노드의 구성 요소: key, nextlink, prevlink
# 필요 이유: popback, pushback 을 할때 O(n)만큼의 시간이 소요되는것을 극복하기 위함
# head 노드는 tail 노드가 next 노드가되고 tail 노드는 head 노드가 next 가 되도록 구현
# 더미노드(헤드노드) 가 필요함 key 값으로 None을 가진 사실 초기화 입장에서 필요한거같다 더미노드는

# 삽입, 삭제 시 splice 연산을 자주 사용
# splice 연산이란? def splie(self, a,b,x) abx=노드 를 받고 a~ b 를 컷 해서 x 와 x next 노드 사이에 삽입하는것
# 조건 a와 b 사이에 헤드노드, x 노드가 있으면 안된다 

# 이동연산인 move after move before 연산에 splice 함수 호출하는식으로 사용하네
# insert 할때도 moveafter 호출하는식으로 한다
# pushfront 는 insert 호출


# 한방향 연결리스트 구현
"""

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head_node = Node()
        self.size = 0
    
    def pushfront(self, val):
        if len(self) == 0:
            self.head_node.key = val
        else:
            v = Node(val)
            v.next_node = self.head_node
            self.head_node = v
        self.size += 1
    
    def popfront(self):
        if len(self) == 0:
            return None
        else:
            v = self.head_node.next_node
            key = self.head_node.key
            del self.head_node
            self.head_node = v
        self.size -= 1
        return key
    
    def pushtail(self, val):
        if len(self) == 0:
            self.head_node.key = val
        else:
            v = self.head_node
            while v.next_node != None:
                v = v.next_node
            v.next_node = Node(val)
        self.size += 1
    
    def poptail(self):
        if len(self) == 0:
            return None
        else:
            prev = None
            v = self.head_node
            
            while v.next_node != None:
                prev = v
                v = v.next_node
            prev.next_node = None
        self.size -= 1
        pass
    
    def __len__(self):
        return self.size
        
    def gen(self):
        v = self.head_node
        while(v.next_node != None):
            yield v
            v = v.next_node
        return
    
L = LinkedList()
L.pushfront("abc")
L.pushfront("11")
L.popfront()
L.pushtail(222)
L.pushtail(444)
L.poptail()

v = L.head_node
while v != None:
    print(v.key)
    v = v.next_node
"""


# 양방향 연결리스트 구현
