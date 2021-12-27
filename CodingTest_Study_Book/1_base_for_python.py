## 수 자료형
# 실수표기에의한 오차 발생으로 round 함수 사용
# a = 0.3 + 0.6

# print(round(a, 1))

##list 자료형
#list 관련 메서드의 시간복잡도
#append O(1)
#sort O(nlogn)
#list = [1,2,5,2,3]
#list.sort(reverse=True)

#reverse O(N)
#insert O(N) : insert 를 남발하는경우 append 에 비해 동작 시간이 많이 느려질 수 있음
#count O(N) : 특정한 값을 가지는 데이터의 갯수
#remove O(N) : 가진 원소가 여러개인 경우 하나만 제거한다
# remove에서 특정 항목을 모두 삭제하는 방법
# a = [1,2,3,3,5,5]
# remove_set = [3,5]
# result = [i for i in a if i not in remove_set]
# print(result)


## 문자열
# 문자열 중 a = "" 형태로 초기화하는 경우 None 이 아니다
# 문자열 또한 list 와 동일하게 slice 사용가능 (순차자료구조)

##튜플
# 리스트에비해 공간 효율적, 각 원소들은 변경 불가능

##딕셔너리
# 키 값 쌍으로 저장 {} 또는 dict()를 통해 초기화 key값은 중복 불가하다
# 내부적으로 해시테이블을 이용하기에 데이터 검색, 수정에 있어 O(1)의 시간복잡도를 가짐
# 키 값 쌍으로 이루어진 데이터를 처리할 때 리스트보다 훨씬 빠르게 동작한다.
# 대표적 함수는 keys() 와 values 함수가 존재 키와 값 데이터만을 가져와서 리스트로 반환
# a = {1:"2", 2:4, 3:3}
# if 1 in a:
#     print("exist")
# for key in a.keys():
#     print(a[key])

##집합 자료형 set
# dict와 동일하게 검색, 수정 모두 시간복잡도 O(1)
# 중복을 허용하지 않고 순서가 없다  순서가 없기에 인덱싱으로 값 접근 불가
# 초기화 방법 1. set([]) 2. {,}
# 특정 데이터가 이미 등작한적 있는지 여부체크할때 효율적?
# 집합 자료형의 연산 & 교집합 | 합집합 - 차집합
# 주요 함수 remove, add, update([])

# 연산자 #and #or #not  #in #not in
# 파이썬은 예외적으로 if 0 <= x < 10 형태의 연산을 허용한다.

## 함수
# 함수 외부의 전역변수에 접근하려면 global 을 사용 (인터프리터 언어 특성 상 전역변수는 함수 위에 위치해야함)
# 람다 (lambda 매개변수,매개변수: 식 )(매개변수, 매개변수)

## 입 출력
# 각 언어별 입력 속도가 빠른 lib 존재 python 의 경우 input 대신 sys.stdin.readline().rstrip() 존재
# print("a" + 7 + "b") 하면 오류 발생 str(7) 을 해주어야함 //문자열과 int 형은 + 연산 불가
# , , 로 구분해주는것도 방법 print("a", 7, "b") , 를 사용하는ㄴ경우 의도치않게 공백이 추가될 수 있음
# fstring을 사용하는것도 좋음 print(f"a{7}b")

# 주요 라이브러리 문법과 유의점
# python 라이브러리 참고 사이트 docs.python.org

#기본 내장함수 sum min max sorted
# sorted 응용
# sort 와 다르게 list. 형태가 아님에 유의
# a = [('홍길동',10),('정상훈',22), ('가나다',5)]
# result = sorted(a, key=lambda x : x[1], reverse=True)
# print(result)

## 표준 라이브러리 itertools 
# 리스트에 존재하는 수를 이용해 모든 수열을 가져온다
#from itertools import combinations, combinations_with_replacement, permutations, product

#a = [1,2,3,5]
# print(a)

#중복 비허용
#print(list(permutations(a))) 순서따지면서
#print(list(combinations(a,2))) 순서 따지지않고

# 중복 허용
# print(list(product(a,repeat=2))) 순서 따지면서
# print(list(combinations_with_replacement(a,2))) 순서 따지지않고


## heapq 힙 기능을 제공하는 라이브러리 모듈
# 파이썬의 힙은 최소힙으로 구현되어있어 heapq에 넣었다 빼는것만으로도 오름차순 정렬이 완료된다 
# heapify up 을 n 개만큼 정렬하기 때문에 시간복잡도 O(nlogn)
# heapq 를 통해 heap 정렬하는 예제코드

# 좀 헷갈리는게 heappush 한다음 그대로 그리스트를 출력하면어캐되는거지?
# => heap 형태의 리스트가 만들어진다 다시 heappop 해서 하나씩 꺼내야 정렬된 list를 얻을 수 있다.
# 너무 신기해!!!!!!!
# import heapq
# def heapsort(iter):
#     h = []
#     result = []
#     for value in iter:
#         heapq.heappush(h,value)
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result

# result = heapsort([1,9,6,2,3,4,6])
# print(result)

# 추가로 python 의 heapq 의 경우 maxheap 을 지원하지 않으므로 원소에 - 를 붙여 push 한 후 pop 할때 다시 - 를 붙이는 형식을 사용한다
# 또는 heapq.heappush(list, (-item, item)) 형식으로 삽입을 할 경우, 튜플의 첫번째 원소를 기준으로 push 하기떄문에 maxheap 형태로 삽입이 된다.

# 라이브러리 이용하지 않고 힙 구현
# 참고사이트 https://jiwon-lee-it.tistory.com/113
# 삽입 삭제 시 O(logn) 만큼의 시간 소요
# 일단 makeheap 제외하고 삽입삭제기능 만들어보자

# class MaxHeap:
#     def __init__(self):
#         self.tree = [None]
#         # list -> heap 으로 만들고싶은경우 insert를 리스트갯수만큼 하면 됨
        
#     def __len__(self):
#         return len(self.tree) - 1
    
#     def insert(self, val):
#         self.tree.append(val)
#         self.heapify_up(len(self))
#         pass            
    
#     def heapify_up(self, i):
#         parentidx = i//2
        
#         while 0 < parentidx:
#             if self.tree[i] > self.tree[parentidx]:
#                 #swap
#                 self.tree[i], self.tree[parentidx] = self.tree[parentidx], self.tree[i]
#                 i = parentidx
#                 parentidx = i//2
#             else:
#                 break;
        
#     def pop(self):
#         result = None
        
#         if len(self) > 0:
#             self.tree[len(self)], self.tree[1] = self.tree[1], self.tree[len(self)]
#             result = self.tree.pop()
#             self.heapify_down(1)
#         else:
#             result = None
        
#         return result
    
#     def heapify_down(self, i):
#         left = i * 2
#         right = i * 2 + 1
#         max = i
        
#         if left <= len(self) and self.tree[max] < self.tree[left]:
#             max = left
        
#         if right <= len(self) and self.tree[max] < self.tree[right]:
#             max = right
        
#         if max != i:
#             self.tree[i], self.tree[max] = self.tree[max], self.tree[i]
#             self.heapify_down(max)
    
#     def printheap(self):
#         print(self.tree[1:])

# h = MaxHeap()
# h.insert(1)
# h.insert(14)
# h.printheap()
# h.pop()
# h.printheap()

## bisect 라이브러리
# 이진탐색을 쉽게 구현할 수 있는 라이브러리
# bisect_left, bisect_right
# 정렬된 리스트에서 특정 범위에 속하는 원소의 갯수 를 구하고자할때 O(logN) 시간이 소요되므로 효율적


##collections 라이브러리
# 유용한 자료구조 제공 코테에서 주로 사용되는 클래스는 deque와 Counter
# deque의 경우 첫번째, 마지막 인덱스의 삽입, 삭제 연산이 O(1) 소요 (스택, 큐 구현가능)
# Counter는 iterable 객체가 주어졌을 때 그게 몇번 등장하는지 알려줌
# from collections import Counter
# a = [133,2,2,2,2,2]
# c = Counter(a)
# print(c[2])

##math 라이브러리
# 수학 계산과 관련된 유용한 클래스 제공 factorial, 제곱근(sqrt), 최대공약수(gcd), 최소공배수(lcm) 등