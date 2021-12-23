# 트리 -> 관계형 자료구조
# 리스트에서 자료에 접근할 때 순차적으로 접근하는경우 O(n)만큼의 시간이 소요될 수 있음을 극복하기 위함
# 보통 이진트리를 많이 사용 (최대 자식노드를 2개까지 가질 수 있는 트리)
# level : root 노드의 level = 0

# 표현법
# 1. 배열공간에 저장하는 방식 (빈 공간도 있음)
# 2. 배열공간에 재귀적으로 표현하는 방식
# 3. 노드 class를 정의하는 방식 (키, parent, right, left 자식노드)


# 1. 배열공간 저장의 장점
# H[n] 의 왼쪽 자식노드 -> 2 * n +1  오른쪽 자식노드 2 * n + 2
# *2의 이유는 레벨별로 자식2개의 공간이 늘어나기때문

# H[n] 의 부모노드 -> 왼쪽노드 인 경우 (n-1)/2   오른쪽 노드인경우 (n-2)/2

# 부모, 자식노드를 찾는거는 상수시간 소요
# 힙 = 이진트리를 배열로 표현했을 때 꽉 차있는경우를 의미